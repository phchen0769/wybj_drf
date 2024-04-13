import django_filters
from .models import Article


class ArticlesFilter(django_filters.FilterSet):
    """
    文章过滤类
    """

    # 根据最小、最大排名进行过滤
    ranking_min = django_filters.NumberFilter(field_name="ranking", lookup_expr="gte")
    ranking_max = django_filters.NumberFilter(field_name="ranking", lookup_expr="lte")

    class Meta:
        model = Article
        fields = ["ranking_min", "ranking_max"]
