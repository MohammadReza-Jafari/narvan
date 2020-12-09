from django.urls import path, include

from core import views

app_name = 'calculator'
urlpatterns = [
    path('calculate/', include(
        [
            path('fibonacci/', views.FibonacciView.as_view(), name='fibonacci'),
            path('factorial/', views.FactorialView.as_view(), name='factorial'),
            path('ackermann/', views.AckermannView.as_view(), name='ackermann')
        ]
    ))
]