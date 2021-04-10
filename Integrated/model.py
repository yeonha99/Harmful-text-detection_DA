import torch
import param
import torch.nn as nn
from transformers import BertModel, DistilBertModel, RobertaModel
from tokenization_kobert import KoBertTokenizer

class BertEncoder(nn.Module):
    def __init__(self):
        super(BertEncoder, self).__init__()
        self.encoder = BertModel.from_pretrained('bert-base-multilingual-cased')

    def forward(self, x, mask=None):
        outputs = self.encoder(x, attention_mask=mask)
        feat = outputs[1]
        return feat


class DistilBertEncoder(nn.Module):
    def __init__(self):
        super(DistilBertEncoder, self).__init__()
        self.encoder = DistilBertModel.from_pretrained('distilbert-base-multilingual-cased')
        self.pooler = nn.Linear(param.hidden_size, param.hidden_size)

    def forward(self, x, mask=None):
        outputs = self.encoder(x, attention_mask=mask)
        hidden_state = outputs[0]
        pooled_output = hidden_state[:, 0]
        feat = self.pooler(pooled_output)
        return feat


class KobertEncoder(nn.Module):
    def __init__(self):
        super(KobertEncoder, self).__init__()
        self.encoder = BertModel.from_pretrained('monologg/kobert')

    def forward(self, x, mask=None):
        outputs = self.encoder(x, attention_mask=mask)
        feat = outputs[1]
        return feat


class DistilKobertEncoder(nn.Module):
    def __init__(self):
        super(DistilKobertEncoder, self).__init__()
        self.encoder = DistilBertModel.from_pretrained('monologg/distilkobert')
        self.pooler = nn.Linear(param.hidden_size, param.hidden_size)

    def forward(self, x, mask=None):
        outputs = self.encoder(x, attention_mask=mask)
        hidden_state = outputs[0]
        pooled_output = hidden_state[:, 0]
        feat = self.pooler(pooled_output)
        return feat


class BertClassifier(nn.Module):
    def __init__(self, dropout=0.1):
        super(BertClassifier, self).__init__()
        self.dropout = nn.Dropout(p=dropout)
        self.classifier = nn.Linear(param.hidden_size, param.num_labels)
        self.apply(self.init_bert_weights)

    def forward(self, x):
        x = self.dropout(x)
        out = self.classifier(x)
        return out

    def init_bert_weights(self, module):
        if isinstance(module, (nn.Linear, nn.Embedding)):
            module.weight.data.normal_(mean=0.0, std=0.02)
        if isinstance(module, nn.Linear) and module.bias is not None:
            module.bias.data.zero_()


class Discriminator(nn.Module):
    """Discriminator model for source domain."""

    def __init__(self):
       
        super(Discriminator, self).__init__()
        self.layer = nn.Sequential(
            nn.Linear(param.hidden_size, param.intermediate_size),
            nn.LeakyReLU(),
            nn.Linear(param.intermediate_size, param.intermediate_size),
            nn.LeakyReLU(),
            nn.Linear(param.intermediate_size, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        out = self.layer(x)
        return out
