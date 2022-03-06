from django.db import models


# Create your models here.


class Audio(models.Model):
    artiste = models.CharField(max_length=100)
    identification_code= models.CharField(max_length=30,unique=True)
    title= models.CharField(max_length=30)
    description= models.TextField(max_length=300)
    audio_file= models.FileField(upload_to="audio")
    cover_picture= models.FileField(upload_to="cover_picture")

    def __str__(self):
        return f"{self.artiste},{self.identification_code},{self.title},{self.description},{self.audio_file},{self.cover_picture}"

class Video(models.Model):
    artiste = models.CharField(max_length=100)
    identification_code = models.CharField(max_length=30, unique=True)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    video_file = models.FileField(upload_to="video")

class Artiste(models.Model):
    artiste = models.CharField(max_length=100)
    identification_code = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=300)
    artiste_picture = models.FileField(upload_to="artiste_picture")






# import secrets
# from django.db import models
# from .paystack import PayStack
#
#
#
# class Payment(models.Model):
#     amount = models.PositiveIntegerField()
#     ref = models.CharField(max_length=200)
#     email = models.EmailField()
#     verified = models.BooleanField(default=False)
#     date_created = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ("-date_created",)
#
#
#     def __str__(self) -> str:
#         # return f"Payment: {self.amount}"
#         return f"{self.email} - {self.amount} - {self.ref} - {self.date_created}"
#
#     def save(self, *args, **kwargs) -> None:
#         while not self.ref:
#             ref = secrets.token_urlsafe(50)  # secrets model is used to generate a safe api key
#             object_with_similar_ref = Payment.objects.filter(ref=ref)
#             if not object_with_similar_ref:
#                 self.ref = ref
#                 print("This is the original ref: ",self.ref)
#         super().save(*args, **kwargs)
#
#
#     def amount_value(self) -> int:  # a work around for a decimal part in amount
#         return self.amount * 100
#
#     def verify_payment(self):
#         paystack = PayStack()
#         status, result = paystack.verify_payment(self.ref, self.amount)
#         if status:
#             if result["amount"] / 100 == self.amount:
#                 self.verified = True
#             self.save()
#         if self.verified:
#             return True
#         return False