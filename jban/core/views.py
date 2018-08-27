from django.http import JsonResponse


def main(request):
    return JsonResponse({"data": {"char_skills": [2, 1]}})
