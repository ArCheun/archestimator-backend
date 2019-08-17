from django.contrib.auth.models import User

from estimator.models import Phase


def get_records(request):
    """
    Returns the Phase objects accessible by the user making the given request

    :param request: request object
    :type request: Request
    :return:
    """
    user = request.user  # type:User
    if user.groups.filter(name='Project Admins').exists():
        return Phase.objects.all()

    return Phase.objects.filter(resources__user__username=user)


def get_estimates(request, phase_id):
    """
    Returns the Estimate objects, created for the given Phase and which are owned by the user making the given request

    :param phase_id: pk of the Phase to consider
    :param request: request object
    :type request: Request
    :return:
    """
    user = request.user  # type:User
    if user.groups.filter(name='Project Admins').exists():
        return Phase.objects.get(pk=phase_id).estimate_set.all()

    return Phase.objects.get(pk=phase_id).estimate_set.filter(user)
