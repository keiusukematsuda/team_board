from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.core.paginator import Paginator

from .forms import EventForm
from .models import Event, Comment, Attend


class EventListView(View):
    def get(self, request, *args, **kwargs):
        all_events = Event.objects.order_by('-created_at')
        paginate_by = 10
        paginator = Paginator(all_events, paginate_by)
        p = request.GET.get('p')
        events = paginator.get_page(p)
        return render(request, 'proto1/event_list.html', {'events': events})


class EventDetailView(View):
    def get(self, request, *args, **kwargs):
        event = get_object_or_404(Event, pk=kwargs['event_id'])
        all_comments = Comment.objects.all().filter(event=event)
        paginate_by = 10
        paginator = Paginator(all_comments, paginate_by)
        p = request.GET.get('p')
        comments = paginator.get_page(p)
        # eventに紐づくattendを取得する(ユーザ一覧表示用)
        try:
            attends = Attend.objects.all().filter(event=event)
        except Attend.DoesNotExist:
            attends = None

        # eventとユーザに紐づくattendを取得する
        try:
            attend = Attend.objects.get(event=event, user=self.request.user)
        # まだ該当するAttendインスタンスが作成されていない場合は、attendにNoneを入れて返す
        except Attend.DoesNotExist:
            attend = None
        return render(request, 'proto1/event_detail.html', {'event': event, 'attends': attends, 'attend': attend, 'comments': comments})

    def post(self, request, *args, **kwargs):
        event = get_object_or_404(Event, pk=kwargs['event_id'])

        #POSTの中身により処理を分岐させる
        if "attend_state" in request.POST:
            #POSTの中身がattend_stateの場合 => Attendの作成、Eventの更新
            if not Attend.objects.filter(event=event, user=self.request.user).exists():
                try:
                    attend = Attend.objects.create(
                        attend_state=request.POST["attend_state"],
                        event=event,
                        user=self.request.user,
                    )
                    # attend_stateをもとにEventのnum_Xを更新する
                    # 今後は例外処理もいれる
                    self.countup(event, attend.attend_state)
                    event.save()
                    attend.save()
                    return redirect('proto1:event_detail', event_id=event.id)
                except:
                    # エラーが表示されるようにしたい
                    return redirect('proto1:event_list')
            else:
                # 変更前のstateカウントを減らす
                attend = Attend.objects.get(event=event, user=self.request.user)
                self.countdown(event, attend.attend_state)

                attend_state = request.POST["attend_state"]
                self.countup(event, attend_state)
                Attend.objects.filter(event=event, user=self.request.user).update(attend_state=attend_state)
                event.save()
                return redirect('proto1:event_detail', event_id=attend.event.id)

        elif "content" in request.POST:
            #POSTの中身がCommentのcontentの場合 => Commentの作成
            comment = Comment.objects.create(
                event=event,
                content=request.POST["content"],
                commented_by=self.request.user,
            )
            comment.save()
            return redirect('proto1:event_detail', event_id=event.id)


    #eventカウントアップメソッド
    def countup(self, event, attend_state):
        if int(attend_state) == 1:
            event.num_join += 1
        if int(attend_state) == 2:
            event.num_pend_join += 1
        if int(attend_state) == 3:
            event.num_pend_def += 1
        if int(attend_state) == 4:
            event.num_cancel += 1

    #eventカウントダウンメソッド
    def countdown(self, event, attend_state):
        if int(attend_state) == 1:
            event.num_join -= 1
        if int(attend_state) == 2:
            event.num_pend_join -= 1
        if int(attend_state) == 3:
            event.num_pend_def -= 1
        if int(attend_state) == 4:
            event.num_cancel -= 1


class EventRegisterView(View):
    def get(self, request, *args, **kwargs):
        print(request.user)
        return render(request, 'proto1/event.html', {'form': EventForm(initial={'created_by': self.request.user})})

    def post(self, request, *args, **kwargs):
        form = EventForm(request.POST)
        post = form.save(commit=False)
        post.save()

        return redirect('proto1:event_list')


