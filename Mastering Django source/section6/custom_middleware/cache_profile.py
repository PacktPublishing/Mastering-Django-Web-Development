class UserProfileMiddleware:

    def process_request(self, req):
        if not req.user.is_authenticated():
            return None
    
        profile = cache.get('userprofile_%s' % req.user.pk)
    
        if profile is None:
            try:
                profile = UserProfile.objects.get(user=req.user)
                cache.set('userprofile_%s' % req.user.pk, profile)
                
            except UserProfile.DoesNotExist:
                pass
    
        req.profile = profile
    
        return None
