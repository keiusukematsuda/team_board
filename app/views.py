from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

from .filters import EventFilter
from .forms import EventForm
from .models import Event


# Create your views here.
# 検索一覧画面
class EventFilterView(LoginRequiredMixin, FilterView):
    model = Event

    # デフォルトの並び順を新しい順とする
    queryset = Event.objects.all().order_by('-created_at')

    # django-filter用設定
    filterset_class = EventFilter
    strict = False

    # 1ページあたりの表示件数
    paginate_by = 10

    # 検索条件をセッションに保存する
    def get(self, request, **kwargs):
        if request.GET:
            request.session['query'] = request.GET
        else:
            request.GET = request.GET.copy()
            if 'query' in request.session.keys():
                for key in request.session['query'].keys():
                    request.GET[key] = request.session['query'][key]

        return super().get(request, **kwargs)


# 詳細画面
class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event


# 登録画面
class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('index')


# 更新画面
class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('index')


# 削除画面
class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('index')
