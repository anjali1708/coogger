# django
from django.utils.deprecation import MiddlewareMixin
from django.urls import resolve

# models
from core.cooggerapp.models import Content, Topic, UTopic, Commit
from django.contrib.auth.models import User


class HeadMixin:
    def process_request(self, request):
        self.path_info = request.path_info
        invalid = ["sitemap", "api", "robots.txt"]
        if self.path_info.split("/")[1] in invalid:
            return None
        url_name = resolve(self.path_info).url_name
        if url_name is None:
            return None
        self.kwargs = resolve(self.path_info).kwargs
        try:
            request.head = getattr(self, url_name.replace("-", "_"))
        except AttributeError:
            request.head = dict(
                title=url_name.title(),
                keywords=url_name,
                description=url_name,
                image="",
            )


class HeadMiddleware(MiddlewareMixin, HeadMixin):
    def content_detail(self):
        username = self.kwargs.get("username")
        permlink = self.kwargs.get("permlink")
        content = Content.objects.get(user__username=username, permlink=permlink)
        keywords = ""
        for key in content.tags.split():
            keywords += key + ", "
        return dict(
            title=f"{content.utopic.name.capitalize()} | {content.title.capitalize()}",
            keywords=f"{keywords}{content.utopic.name.lower()}",
            description=content.description.capitalize(),
            image=content.image_address
            or "https://www.coogger.com/media/images/coogger_W56Ux33.png",
        )

    def embed(self):
        return self.content_detail()

    def topic(self):
        topic = Topic.objects.filter(permlink=self.kwargs.get("permlink"))[0]
        try:
            description = topic.definition.capitalize()
        except AttributeError:
            description = topic.name
        return dict(
            title=f"{topic.name} - Topic | Coogger".capitalize(),
            keywords=topic.name,
            description=description,
            image=topic.image_address,
        )

    def comment(self):
        username = self.kwargs.get("username")
        return dict(
            title=f"{username} - comment".capitalize(),
            keywords=f"{username}, comment {username}, comment",
            description=f"comment {username}".capitalize(),
            image=None,
        )

    def category(self):
        cat_name = self.kwargs.get("cat_name")
        return dict(
            title=f"Latest post on coogger from {cat_name} category".capitalize(),
            keywords=f"{cat_name}, {cat_name} category",
            description=f"Latest post on coogger from {cat_name} category".capitalize(),
            image="/static/media/topics/category.svg",
        )

    def language(self):
        lang_name = self.kwargs.get("lang_name")
        return dict(
            title=f"{lang_name} language | coogger".capitalize(),
            keywords=f"{lang_name}, language {lang_name}",
            description=f"Latest post on coogger from {lang_name} language".capitalize(),
            image="/static/media/topics/language.svg",
        )

    def user(self):
        username = self.kwargs.get("username")
        user = User.objects.get(username=username)
        return dict(
            title=f"{username} • coogger".capitalize(),
            keywords=f"{username}, coogger {username}",
            description=f"The latest posts from {username} on coogger".capitalize(),
            image=user.githubauthuser.avatar_url,
        )

    def userabout(self):
        username = self.kwargs.get("username")
        user = User.objects.get(username=username)
        return dict(
            title=f"{username} | About".capitalize(),
            keywords=f"about {username}, {username}, about",
            description=f"About of {username}".capitalize(),
            image=user.githubauthuser.avatar_url,
        )

    def detail_utopic(self):
        username = self.kwargs.get("username")
        permlink = self.kwargs.get("permlink")
        user = User.objects.get(username=username)
        utopic = UTopic.objects.filter(user=user, permlink=permlink)[0]
        if utopic.definition:
            definition = f"{utopic.definition.capitalize()} | {username}"
        else:
            definition = f"{username}'s contents about topic of {utopic}"
        if utopic.image_address:
            image = utopic.image_address
        else:
            image = user.githubauthuser.avatar_url
        return dict(
            title=f"{utopic} - Topic | {username}".capitalize(),
            keywords=utopic,
            description=definition,
            image=image,
        )

    def settings(self):
        return dict(
            title="settings",
            keywords="settings,coogger settings",
            description="Coogger settings,",
            image=None,
        )

    def hashtag(self):
        tag = self.kwargs.get("hashtag")
        return dict(
            title=f"coogger lates post from '{tag}' hashtag.",
            keywords=f"{tag}",
            description=f"coogger lates post from '{tag}' hashtag.",
            image="/static/media/icons/list.svg",
        )

    def explorer_posts(self):
        return dict(
            title=f"coogger",
            keywords=f"coogger, developers, experience, documentation, blogs, projects",
            description="""
                Coogger is a platform where developers can write their knowledge,
                experience, documentation and blogs about their projects or projects which love.""",
            image="https://www.coogger.com/static/logos/png/800.png",
        )

    def home(self):
        return self.explorer_posts()

    def issues(self):
        username = self.kwargs.get("username")
        utopic_permlink = self.kwargs.get("utopic_permlink")
        user = User.objects.get(username=username)
        title = f"{utopic_permlink}/{username} | issues".capitalize()
        return dict(
            title=title,
            keywords=f"{utopic_permlink}, {username}",
            description=title,
            image=user.githubauthuser.avatar_url,
        )

    def detail_issue(self):
        username = self.kwargs.get("username")
        utopic_permlink = self.kwargs.get("utopic_permlink")
        permlink = self.kwargs.get("permlink")
        user = User.objects.get(username=username)
        title = f"{utopic_permlink}/{username} - {permlink} | issue".capitalize()
        return dict(
            title=title,
            keywords=f"{utopic_permlink}, {username}",
            description=title,
            image=user.githubauthuser.avatar_url,
        )

    def commits(self):
        username = self.kwargs.get("username")
        topic_permlink = self.kwargs.get("topic_permlink")
        user = User.objects.get(username=username)
        title = f"{topic_permlink}/{username} | commits".capitalize()
        return dict(
            title=title,
            keywords=f"{topic_permlink}, {username}",
            description=title,
            image=user.githubauthuser.avatar_url,
        )

    def commit(self):
        username = self.kwargs.get("username")
        topic_permlink = self.kwargs.get("topic_permlink")
        hash = self.kwargs.get("hash")
        commit = Commit.objects.get(hash=hash)
        user = User.objects.get(username=username)
        title = f"{topic_permlink}/{username} - {commit.msg} | commit".capitalize()
        return dict(
            title=title,
            keywords=f"{topic_permlink}, {username}, {commit.msg}, commit",
            description=title,
            image=user.githubauthuser.avatar_url,
        )

    def feed(self):
        username = self.kwargs.get("username")
        user = User.objects.get(username=username)
        title = f"{username}'s Feed".capitalize()
        return dict(
            title=title,
            keywords=f"{username}, feed",
            description=title,
            image=user.githubauthuser.avatar_url,
        )
