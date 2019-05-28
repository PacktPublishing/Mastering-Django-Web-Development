
class UserProfileMiddleware:
    def process_request(self, request):
        if not request.user.is_authenticated():
            return None

        profile = cache.get('userprofile_%s' % request.user.pk)

        if profile is None:
            try:
                profile = UserProfile.objects.get(user=request.user)
                cache.set('userprofile_%s' % request.user.pk, profile)

            except UserProfile.DoesNotExist:
                profile = EmptyProfile() # replace this line with working code

        request.profile = profile

        return None
