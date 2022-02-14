from dal import autocomplete
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render
from loguru import logger
from taggit.models import Tag

from core.forms import ExperiencePageForm
from core.models import (
    ExperiencePage,
    HomePage,
    ExperiencesPage,
    ExperiencesCategory,
)
from core.utils.helper import unique_slug_generator


@login_required
def submit_experience(request: HttpRequest, home_page: HomePage):
    if request.method == "POST":
        form = ExperiencePageForm(request.POST)
        if form.is_valid():
            logger.debug(f"Saving new exp {form.cleaned_data}")
            new_exp_page: ExperiencePage = form.save(commit=False)
            new_exp_page.slug = unique_slug_generator(new_exp_page)
            new_exp_page.tags.add(*form.cleaned_data["tags"])
            selected = form.cleaned_data["categories"]
            if selected:
                new_exp_page.categories.clear()
                for cat in selected:
                    new_exp_page.categories.add(cat)
            new_exp_page.owner = request.user
            new_exp: ExperiencePage = ExperiencesPage.objects.all()[0].add_child(
                instance=new_exp_page
            )
            if new_exp:
                new_exp.unpublish()
                new_exp.save_revision(submitted_for_moderation=True, user=request.user)
            return render(
                request, "core/after_submit.html", {"exp_name": new_exp.title}
            )

    else:
        form = ExperiencePageForm()

    return render(
        request,
        "core/submit_experience_page.html",
        {
            "form": form,
        },
    )


@login_required
def edit_experience(request: HttpRequest, experience_page: ExperiencePage):
    if request.method == "POST":
        form = ExperiencePageForm(request.POST, instance=experience_page)
        if form.is_valid():
            selected = form.cleaned_data["categories"]
            if selected:
                experience_page.categories.clear()
                for cat in selected:
                    experience_page.categories.add(cat)
            experience_page.save_revision(
                submitted_for_moderation=True, user=request.user, changed=True
            )
            return render(
                request,
                "core/after_submit.html",
                {"exp_name": experience_page.title, "after_edit": True},
            )
    else:
        return render(
            request,
            "core/submit_experience_page.html",
            {
                "form": ExperiencePageForm(instance=experience_page),
            },
        )
# to sort tags based on how many time its used
# >>> a = ExperiencePageTag.objects.values_list('tag_id').annotate(tag_count=Count('tag_id')).order_by('-tag_count')
# >>> [Tag.objects.get(id=i[0]) for i in a]

class CategoriesAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = ExperiencesCategory.objects.all().order_by('id')
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs


class TagsAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Tag.objects.all().order_by('id')
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
            return qs
        return qs[0:10]
