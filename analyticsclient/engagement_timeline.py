import urllib
from analyticsclient.base import PostableCourseIDsEndpoint
from analyticsclient.constants import data_formats


class EngagementTimeline(PostableCourseIDsEndpoint):
    """Engagement Timeline."""

    def __init__(self, client, username, course_id):
        """
        Initialize the EngagementTimeline client.

        Arguments:

            client (analyticsclient.client.Client): The client to use to access remote resources.
            username (str): String identifying the user (e.g. jbradley)
            course_id (str): String identifying the course (e.g. edX/DemoX/Demo_Course)

        """
        super(EngagementTimeline, self).__init__(client)

        self.username = unicode(username)
        self.course_id = unicode(course_id)

    def get(self):
        """Get a particular learner's engagement timeline for a particular course."""
        querystring = urllib.urlencode({'course_id': self.course_id})
        path = 'engagement_timelines/{username}/?{querystring}'.format(username=self.username, querystring=querystring)
        return self.client.get(path, data_format=data_formats.JSON)
