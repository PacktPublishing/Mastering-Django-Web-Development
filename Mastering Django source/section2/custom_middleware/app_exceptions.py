
class AppExceptionTrap:
    def process_exception(self, request, exception):

        if isinstance(exception, AppError):
            messages.error(request, str(exception))

            return HttpResponseRedirect('/')

        return None