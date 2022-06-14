from django.db import models
from rest_framework.response import Response


class RoadmapManager(models.Manager):

    def userstudy_progress(self, tech, topic, customer, is_done):
        userstudy = self.get_or_create(user=customer, technology=tech)[0]
        topics = userstudy.topics.all()
        num_topics = tech.topics.count()
        percent = 100 / num_topics

        if is_done:
            if userstudy.progress < 100 and topic not in topics:
                userstudy.topics.add(topic)
                customer.skill.add(*topic.skills.all().values_list('id', flat=True))
                userstudy.progress += percent
                userstudy.save()
        else:
            if userstudy.progress > 0 and topic in topics:
                userstudy.topics.remove(topic)
                customer.skill.remove(*topic.skills.all().values_list('id', flat=True))
                userstudy.progress -= percent
                userstudy.save()
        userstudy_progress = userstudy.progress
        return Response({
            "customer": customer.full_name,
            "email": customer.email,
            "technology": tech.name,
            "topic": topic.name,
            "total_percent": round(userstudy_progress),
            "added_percent" if is_done else "removed": round(percent),
            "done": True if userstudy_progress >= 100 else False,
        })