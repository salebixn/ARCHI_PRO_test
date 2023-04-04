from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Answer, Results, Persons


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['answers'] = Answer.objects.all()

        return context
    

class ResultHandler(TemplateView):
    template_name = 'result.html'
    
    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        user_ie = 0; # это бал EI
        user_sn = 0; # это бал SN
        user_tf = 0; # это бал TF
        user_jp = 0; # это бал JP

        user_i = 'I'; # это буква min для EI экстраверсия-интроверсия (Е-I, от англ. Extravertion-Intmvertion)
        user_n = 'N'; # это буква min для SN сенсорика-интуиция (S-N, от англ. Sensation-Intuition)
        user_f = 'F'; # это буква min для TF логичность-чувствование (T-F, от англ. Thinking-Feeling)
        user_p = 'P'; # это буква min для JP решение-восприятие (J-P, от англ. Judging-Perceiving) (планирование-импульсивность)

        # Рассчёт результата
        for key in self.request.POST.keys():
            if key not in ('csrfmiddlewaretoken', 'name', 'phone', 'email'):
                if int(key.split('-')[-1]) in (1, 8, 15, 22, 29, 36, 43, 50, 57, 64):
                    if self.request.POST.get(key) == 'a': user_ie += 1
                elif int(key.split('-')[-1]) in (2, 9, 16, 23, 30, 37, 44, 51, 58, 65,
                                                 3, 10, 17, 24, 31, 38, 45, 52, 59, 66):
                    if self.request.POST.get(key) == 'a': user_sn += 1
                elif int(key.split('-')[-1]) in (4, 11, 18, 25, 32, 39, 46, 53, 60, 67,
                                                 5, 12, 19, 26, 33, 40, 47, 54, 61, 68):
                    if self.request.POST.get(key) == 'a': user_tf += 1
                elif int(key.split('-')[-1]) in (6, 13, 20, 27, 34, 41, 48, 55, 62, 69,
                                                 7, 14, 21, 28, 35, 42, 49, 56, 63, 70):
                    if self.request.POST.get(key) == 'a': user_jp += 1

        if user_ie > 5: user_i = 'E'
        else: user_i = 'I'
        if user_sn > 10: user_n = 'S'
        else: user_n = 'N'
        if user_tf > 10: user_f = 'T'
        else: user_f = 'F'
        if user_jp > 10: user_p = 'J'
        else: user_p = 'P'

        user_nnnn = user_i + user_n + user_f + user_p
                    
        user_nnnn = Results.objects.get(name=user_nnnn)

        score = user_ie + user_sn + user_tf + user_jp

        person = Persons(name=self.request.POST.get('name'), phone=int(self.request.POST.get('phone')),
                         email=self.request.POST.get('email'), result=user_nnnn, score=score,
                         user_ie=user_ie, user_sn=user_sn, user_tf=user_tf, user_jp=user_jp)
        person.save()


        context['person'] = person

        return render(request, 'result.html', context)