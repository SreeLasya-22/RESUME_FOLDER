from django.shortcuts import render, redirect, get_object_or_404
from .forms import ResumeForm
from .models import Resume
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML

# ----------------------------
# Resume Form View
# ----------------------------
def resume_form(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save()
            # Redirect to preview page after saving
            return redirect('resume_preview', resume_id=resume.id)
    else:
        form = ResumeForm()
    return render(request, 'resume_form.html', {'form': form})


# ----------------------------
# Resume Preview View
# ----------------------------
def resume_preview(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)

    # Split skills and experience
    skills_list = resume.skills.split(" ") if resume.skills else []
    experience_list = resume.experience.split("\n") if resume.experience else []

    # Check which template to use (default template1)
    template_name = request.GET.get('template', 'template1')
    if template_name not in ['template1', 'template2','template3']:
        template_name = 'template1'

    html_template = f"{template_name}.html"

    context = {
        'resume': resume,
        'skills_list': skills_list,
        'experience_list': experience_list
    }

    return render(request, html_template, context)


# ----------------------------
# PDF Download View
# ----------------------------
def download_resume_pdf(request, resume_id):
    try:
        resume = get_object_or_404(Resume, id=resume_id)

        # Choose template
        template_name = request.GET.get('template', 'template1')
        if template_name not in ['template1', 'template2']:
            template_name = 'template1'

        template_file = f"{template_name}.html"

        # Prepare data
        skills_list = resume.skills.split(" ") if resume.skills else []
        experience_list = resume.experience.split("\n") if resume.experience else []

        context = {
            'resume': resume,
            'skills_list': skills_list,
            'experience_list': experience_list,
            'request': request
        }

        html_string = render_to_string(template_file, context)

        pdf_file = HTML(string=html_string, base_url=request.build_absolute_uri()).write_pdf()

        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{resume.name}_resume.pdf"'
        return response

    except Exception as e:
        print("PDF generation error:", e)
        return HttpResponse("Error generating PDF.", status=500)
