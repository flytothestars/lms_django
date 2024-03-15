from django.core.exceptions import ObjectDoesNotExist  # noqa
from django.db.models.signals import post_delete, post_save  # noqa
from django.dispatch import receiver  # noqa

from courses.models import CourseSession, CourseSessionListener  # noqa
from enrollees.models import TempEnrollee  # noqa


# @receiver(post_save, sender=TempEnrollee)
# def add_listener(sender, instance, created, **kwargs):
#     def add_session_listener(session, listener):
#         course_listener = CourseSessionListener(
#             course_session=session, listener=listener
#         )
#         course_listener.save()

#     if created:
#         course_session = CourseSession.objects.filter(
#             course_schedule=instance.course_schedule
#         ).first()
#         if course_session:
#             add_session_listener(course_session, instance)
#         else:
#             course_session = CourseSession(course_schedule=instance.course_schedule)
#             course_session.save()
#             add_session_listener(course_session, instance)
