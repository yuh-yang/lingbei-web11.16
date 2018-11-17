from django.db import models
from gensim import corpora, models, similarities
import jieba

# Create your models here.
class UserInfo (models.Model):
    username = models.TextField()
    password = models.TextField()

    def __unicode__(self):
        return self.username

class Tweet(models.Model):
    username = models.TextField()
    date = models.DateField().auto_now_add
    time = models.TextField()
    place = models.TextField()
    thing = models.TextField()
    think = models.TextField()

    def __unicode__(self):
        return self.username, self.date, self.time, self.place

def save_tweets(un,dt,tm,pl,th): #存储一条发布
    Tweet.objects.create(username=un, date=dt, time=tm, place=pl, thing=th)

def contrast(user1, user2): #比较相似性
    '''    按A过去七天的行为，排出各个时间段最常做事+地点前四名。外层按时间段排，内层按常见度排，输入到一个列表 list1 = []
    对B同样，得到list2 = []
   对两个列表进行文本相似度分析。'''
    text1 = []
    text2 = []
    # 1、将【文本1】生成【分词列表】
    texts1 = [jieba.cut(text1) for text in text1]
    # 2、基于文本集建立【词典】，并提取词典特征数
    dictionary = corpora.Dictionary(texts1)
    feature_cnt = len(dictionary.token2id.keys())
    # 3、基于词典，将【分词列表集】转换成【稀疏向量集】，称作【语料库】
    corpus = [dictionary.doc2bow(text) for text in texts1]
    # 4、使用【TF-IDF模型】处理语料库
    tfidf = models.TfidfModel(corpus)
    # 5、同理，用【词典】把【搜索词】也转换为【稀疏向量】
    kw_vector = dictionary.doc2bow(jieba.cut(text2))
    # 6、对【稀疏向量集】建立【索引】
    index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=feature_cnt)
    # 7、相似度计算
    sim = index[tfidf[kw_vector]]
    return sim




