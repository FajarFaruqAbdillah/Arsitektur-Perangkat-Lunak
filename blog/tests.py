from django.test import SimpleTestCase
from django.urls import reverse


class BlogHomeTests(SimpleTestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse("blog:home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Rangkuman Arsitektur Perangkat Lunak")

    def test_detail_page_loads(self):
        response = self.client.get(
            reverse(
                "blog:post_detail",
                kwargs={"slug": "architectural-quality-attributes"},
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Quality Attributes")
        self.assertContains(response, "Quiz Singkat")
        self.assertContains(response, "data-correct")
        self.assertContains(response, "blog/quiz.js")
