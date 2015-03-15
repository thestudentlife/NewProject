from unittest import TestCase
from django.contrib.auth.models import Permission, User, Group, ContentType
from workflow.models import Profile, Assignment
from mainsite.models import Issue, Section, Article

class WorkflowModels(TestCase):
    def setUp(self):
        from website import initial_data

    def test_initial_data(self):
        kent = Group.objects.all()[3].user_set.all()[0]
        self.assertEqual("kshikama", kent.username)
        print("password for kent: " + kent.password)

        ziqi = Group.objects.all()[3].user_set.all()[1]
        self.assertEqual("zxiong", ziqi.username)
        print("password for ziqi: " + ziqi.password)

        latina = Group.objects.all()[3].user_set.all()[2]
        self.assertEqual("vlatina", latina.username)
        print("password for latina: " + latina.password)

        issue = Issue.objects.all()[0]
        self.assertEqual("SP 2015 1", issue.name)

        profiles = Profile.objects.all()
        for profile in profiles:
            print("profile user: "+profile.user.username)
            print("profile position: "+profile.position)

        sections = Section.objects.all()
        for section in sections:
            print("section name: "+section.name)

        articles = Article.objects.all()
        for article in articles:
            print("article title: "+article.title)
            print("article author: "+article.authors.all()[0].user.username)
            print("article content: "+article.content)
        assignments = Assignment.objects.all()
        for assignment in assignments:
            print("assignment title: "+assignment.title)
            print("assignment content: "+assignment.content)
            print("assignment sender: " +assignment.sender.user.username)
            print("assignment.recipient: "+assignment.receiver.user.username)

    def test_kent_profile(self):
        kent = Group.objects.all()[3].user_set.all()[0]
        kent.first_name = "Kent"
        kent.last_name = "Shikama"

        profile_kent = Profile(user=kent, position='photographer')
        self.assertEqual("Kent Shikama", profile_kent.display_name())