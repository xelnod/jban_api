from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from core.models import Build


# TODO use DRF Luke
def main(request, pk=None):
    build = get_object_or_404(Build, id=pk)
    return JsonResponse({"char_skills": build.skills,
                         "runes": build.runes,
                         "class": build.default_class})


def get_self(request):
    return JsonResponse({"username": "Хзкто"})
