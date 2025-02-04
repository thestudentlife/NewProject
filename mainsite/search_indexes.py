import datetime
from haystack import indexes
from mainsite.models import Article

class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    section = indexes.CharField(model_attr='section')
    title = indexes.CharField(model_attr='title')
    content = indexes.CharField(model_attr='content')
    authors = indexes.MultiValueField()

    def get_model(self):
        return Article

    def prepare_authors(self, object):
        return [profile.display_name for profile in object.authors.all()]

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(published=True).order_by('-published_date')

    def get_updated_field(self):
        return "published_date"
