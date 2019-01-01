from django.test import TestCase
import datetime
from django.utils import timezone
# Create your tests here.
from .models import Question
from django.urls import reverse

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
	

class Quest(TestCase):
    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False) 
 
def create_question(question_text,days):
    return Question.objects.create(question_text=question_text,pub_date=timezone.now()+datetime.delta(days=days))

class QuestionView(TestCase):
    def no_ques(self):
        response=self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, "no poll is here")
        self.assertQuerySetEqual(response.context['latest_question'],[])


    def past_ques(TestCase):
        create_question(question_text="past questions",days=-20)
        response=self.client.get(reverse('polls:index'))
        self.assertQuerySetEqual(response.context['latest_question'],'<Question: past questions>')

    def future_ques(TestCase):
        create_question(question_text='future',days=33)
        response=self.client.get(reverse('polls:index'))
        self.assertContains(response,'polls not here')
        self.assertQuerySetEqual(response.context['latest_question'],[])



                    










