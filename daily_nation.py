import requests
from bs4 import BeautifulSoup


class DailyNation:
    BASE_URL = 'https://www.nation.co.ke'

    @staticmethod
    def get_html(url):
        """
        Get the Daily Nation html
        :return:
        """
        daily_nation = requests.get(url)
        html = BeautifulSoup(daily_nation.text, 'html.parser')
        return html

    @staticmethod
    def get_topics_lis():
        """
        Get all the lis in the nav bar
        :return:
        """
        html = DailyNation.get_html(DailyNation.BASE_URL)
        if html:
            nav = html.find('nav', class_='container')
            topics_ul = nav.find_all('ul')[1]
            return topics_ul.find_all('li')
        return None

    @staticmethod
    def get_topics():
        """
        Get all topics in the nav bar
        :return: list
        """
        lis = DailyNation.get_topics_lis()
        topics = []
        for li in lis:
            topics.append(li.find('a').text.lower())
        return topics

    @staticmethod
    def get_topic_info(topic):
        """
        Get content for a given topic
        :param topic:
        :return:
        """
        topic_url = DailyNation.BASE_URL + DailyNation.get_topics_url()[topic.lower()]
        html = DailyNation.get_html(topic_url)
        if html:
            stories = []
            div_content = html.find('div', class_='five-eight column')
            stories_div = div_content.find_all('div', class_='story-teaser')
            for div in stories_div:
                story = {
                    'title': div.find('a').text, 'summary': div.find('p').text,
                    'story_url': div.find('a').get('href'),
                    'published_at': div.find('h6').text
                }
                if div.find('img'):
                    story['image_url'] = DailyNation.BASE_URL + div.find('img').get('src')
                story['image_url'] = ''
                stories.append(story)
            return stories

    @staticmethod
    def get_data(topic):
        """
        Get topic information based on the topic provided.
        :param topic:
        :return:
        """
        _topic = topic.lower()
        if _topic not in DailyNation.get_topics():
            raise ValueError('Topic does not exist')

        if _topic == 'photos':
            return DailyNation.get_photos(_topic)

        if _topic == 'videos':
            return DailyNation.get_videos(_topic)

        return DailyNation.get_topic_info(_topic)