from django.apps import AppConfig


#class JobBoardConfig(AppConfig):
#    default_auto_field = 'django.db.models.BigAutoField'
#    name = 'job_board'


class JobBoardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'job_board'

    def ready(self):
        from job_board.models import JobPosting
        try:
            job_to_delete = JobPosting.objects.get(title="Job 1")
            job_to_delete.delete()

        except JobPosting.DoesNotExist:
            pass

        try:
            job_to_update = JobPosting.objects.get(title="Data Scientist")
            job_to_update.company = "Tech Innovators"
            job_to_update.save()

        except JobPosting.DoesNotExist:
            pass
