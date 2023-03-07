import os
import openai
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Code
from django.conf import settings


def code_start(request):
    lang_list = [
        "c",
        "clike",
        "cpp",
        "csharp",
        "css",
        "dart",
        "django",
        "go",
        "html",
        "java",
        "javascript",
        "markup",
        "markup-templating",
        "matlab",
        "mongodb",
        "objectivec",
        "perl",
        "php",
        "powershell",
        "python",
        "r",
        "regex",
        "ruby",
        "rust",
        "sass",
        "scala",
        "sql",
        "swift",
        "yaml",
    ]

    if request.method == "POST":
        code = request.POST["code"]
        lang = request.POST["lang"]

        # Check to make sure they picked a lang
        if lang == "Select Programming Language":
            messages.success(request, "Hey! You Forgot To Pick A Programming Language...")
            return render(request, "home.html", {"lang_list": lang_list, "response": code, "code": code, "lang": lang})
        else:
            # OpenAI Key
            openai.api_key = "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"
            # Create OpenAI Instance
            openai.Model.list()
            # Make an OpenAI Request
            try:
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=f"Respond only with code. Fix this {lang} code: {code}",
                    temperature=0,
                    max_tokens=1000,
                    top_p=1.0,
                    frequency_penalty=0.0,
                    presence_penalty=0.0,
                )
                # Parse the response
                response = (response["choices"][0]["text"]).strip()
                # Save To Database
                record = Code(question=code, code_answer=response, language=lang, user=request.user)
                record.save()
                return render(request, "home.html", {"lang_list": lang_list, "response": response, "lang": lang})

            except Exception as e:
                return render(request, "home.html", {"lang_list": lang_list, "response": e, "lang": lang})

    return render(request, "home.html", {"lang_list": lang_list})


def code_suggestion(request):
    lang_list = [
        "c",
        "clike",
        "cpp",
        "csharp",
        "css",
        "dart",
        "django",
        "go",
        "html",
        "java",
        "javascript",
        "markup",
        "markup-templating",
        "matlab",
        "mongodb",
        "objectivec",
        "perl",
        "php",
        "powershell",
        "python",
        "r",
        "regex",
        "ruby",
        "rust",
        "sass",
        "scala",
        "sql",
        "swift",
        "yaml",
    ]

    if request.method == "POST":
        code = request.POST["code"]
        lang = request.POST["lang"]

        # Check to make sure they picked a lang
        if lang == "Select Programming Language":
            messages.success(request, "Hey! You Forgot To Pick A Programming Language...")
            return render(request, "suggest.html", {"lang_list": lang_list, "code": code, "lang": lang, "response": code})
        else:
            # OpenAI Key
            openai.api_key = "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"
            # Create OpenAI Instance
            openai.Model.list()
            # Make an OpenAI Request
            try:
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=f"Respond only with code. Using {lang}. {code}",
                    temperature=0,
                    max_tokens=1000,
                    top_p=1.0,
                    frequency_penalty=0.0,
                    presence_penalty=0.0,
                )
                # Parse the response
                response = (response["choices"][0]["text"]).strip()

                # Save To Database
                record = Code(question=code, code_answer=response, language=lang, user=request.user)
                record.save()

                return render(request, "suggest.html", {"lang_list": lang_list, "response": response, "lang": lang})

            except Exception as e:
                return render(request, "suggest.html", {"lang_list": lang_list, "response": e, "lang": lang})

    return render(request, "suggest.html", {"lang_list": lang_list})

    # def code_suggestion(request):
    #     lang_list = [
    #         "c",
    #         "clike",
    #         "cpp",
    #         "csharp",
    #         "css",
    #         "dart",
    #         "django",
    #         "go",
    #         "html",
    #         "java",
    #         "javascript",
    #         "markup",
    #         "markup-templating",
    #         "matlab",
    #         "mongodb",
    #         "objectivec",
    #         "perl",
    #         "php",
    #         "powershell",
    #         "python",
    #         "r",
    #         "regex",
    #         "ruby",
    #         "rust",
    #         "sass",
    #         "scala",
    #         "sql",
    #         "swift",
    #         "yaml",
    #     ]

    #     if request.method == "POST":
    #         code = request.POST["code"]
    #         lang = request.POST["lang"]
    #         # Check to make sure they picked a lang
    #         if lang == "Select Programming Language":
    #             messages.success(request, "Hey! You Forgot To Pick A Programming Language...")
    #             return render(request, "suggest.html", {"lang_list": lang_list, "code": code, "lang": lang, "response": code})
    #         else:
    #             #    OpenAI Key
    #             openai.api_key = "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"
    #             # Create OpenAI Instance
    #             openai.Model.list()
    #             try:
    #                 # Make an OpenAI Request
    #                 response = openai.Completion.create(
    #                     engine="text-davinci-003",
    #                     prompt=f"Respond only with code. Fix this {lang} code: {code}",
    #                     temperature=0,
    #                     max_tokens=1000,
    #                     top_p=1.0,
    #                     frequency_penalty=0.0,
    #                     presence_penalty=0.0,
    #                 )
    #                 # Parse  the response
    #                 response = (response["choices"][0]["text"]).strip()
    #                 # Save to Database
    #                 res = Code(question=code, code_answer=response, language=lang, user=request.user)
    #                 res.save()
    #                 return render(request, "home.html", {"lang_list": lang_list, "response": response, "lang": lang})

    #             except Exception as e:
    #                 return render(request, "home.html", {"lang_list": lang_list, "response": e, "lang": lang})
    return render(request, "suggestion.html", {"lang_list": lang_list})


def old_code(request):
    if request.user.is_authenticated:
        code = Code.objects.filter(user_id=request.user.id)
        return render(request, "old_code.html", {"code": code})

    else:
        messages.success(request, "You must be logged in to view this page")
        return redirect("home")


def delete_old_code(request, old_id):
    old = Code.objects.get(pk=old_id)
    old.delete()
    messages.success(request, "Deleted successfully")
    return redirect("old")


# def home(request):
# lang_list = [
#     "c",
#     "clike",
#     "cpp",
#     "csharp",
#     "css",
#     "dart",
#     "django",
#     "go",
#     "html",
#     "java",
#     "javascript",
#     "markup",
#     "markup-templating",
#     "matlab",
#     "mongodb",
#     "objectivec",
#     "perl",
#     "php",
#     "powershell",
#     "python",
#     "r",
#     "regex",
#     "ruby",
#     "rust",
#     "sass",
#     "scala",
#     "sql",
#     "swift",
#     "yaml",
# ]

# if request.method == "POST":
#     code = request.POST["code"]
#     lang = request.POST["lang"]

#     # Check to make sure they picked a lang
#     if lang == "Select Programming Language":
#         messages.success(request, "Hey! You Forgot To Pick A Programming Language...")
#         return render(request, "home.html", {"lang_list": lang_list, "response": code, "code": code, "lang": lang})
#     else:
#         # OpenAI Key
#         openai.api_key = "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"
#         # Create OpenAI Instance
#         openai.Model.list()
#         # Make an OpenAI Request
#         try:
#             response = openai.Completion.create(
#                 engine="text-davinci-003",
#                 prompt=f"Respond only with code. Fix this {lang} code: {code}",
#                 temperature=0,
#                 max_tokens=1000,
#                 top_p=1.0,
#                 frequency_penalty=0.0,
#                 presence_penalty=0.0,
#             )
#             # Parse the response
#             response = (response["choices"][0]["text"]).strip()
#             # Save To Database
#             record = Code(question=code, code_answer=response, language=lang, user=request.user)
#             record.save()
#             return render(request, "home.html", {"lang_list": lang_list, "response": response, "lang": lang})

#         except Exception as e:
#             return render(request, "home.html", {"lang_list": lang_list, "response": e, "lang": lang})

# return render(request, "home.html", {"lang_list": lang_list})


# def suggest(request):
#     lang_list = [
#         "c",
#         "clike",
#         "cpp",
#         "csharp",
#         "css",
#         "dart",
#         "django",
#         "go",
#         "html",
#         "java",
#         "javascript",
#         "markup",
#         "markup-templating",
#         "matlab",
#         "mongodb",
#         "objectivec",
#         "perl",
#         "php",
#         "powershell",
#         "python",
#         "r",
#         "regex",
#         "ruby",
#         "rust",
#         "sass",
#         "scala",
#         "sql",
#         "swift",
#         "yaml",
#     ]

#     if request.method == "POST":
#         code = request.POST["code"]
#         lang = request.POST["lang"]

#         # Check to make sure they picked a lang
#         if lang == "Select Programming Language":
#             messages.success(request, "Hey! You Forgot To Pick A Programming Language...")
#             return render(request, "suggest.html", {"lang_list": lang_list, "code": code, "lang": lang, "response": code})
#         else:
#             # OpenAI Key
#             openai.api_key = "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"
#             # Create OpenAI Instance
#             openai.Model.list()
#             # Make an OpenAI Request
#             try:
#                 response = openai.Completion.create(
#                     engine="text-davinci-003",
#                     prompt=f"Respond only with code. Using {lang}. {code}",
#                     temperature=0,
#                     max_tokens=1000,
#                     top_p=1.0,
#                     frequency_penalty=0.0,
#                     presence_penalty=0.0,
#                 )
#                 # Parse the response
#                 response = (response["choices"][0]["text"]).strip()

#                 # Save To Database
#                 record = Code(question=code, code_answer=response, language=lang, user=request.user)
#                 record.save()

#                 return render(request, "suggest.html", {"lang_list": lang_list, "response": response, "lang": lang})

#             except Exception as e:
#                 return render(request, "suggest.html", {"lang_list": lang_list, "response": e, "lang": lang})

#     return render(request, "suggest.html", {"lang_list": lang_list})
