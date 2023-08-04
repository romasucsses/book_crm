class CurrentPageContext:
    mixin_page_name = None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = self.mixin_page_name
        post = self.get_post
        context['post'] = post
        return context

    def get_post(self):
        return None
