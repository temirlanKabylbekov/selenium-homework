# -*- coding: utf-8 -*-
"""PageObject classes."""
import urlparse

from page_elements import AuthForm

from discussion_page_elements import OpenDiscussionLinksChain, \
    LikeCommentInDisscussion, UnlikeCommentInDisscussion, \
    DiscussionCommentLikesController, DiscussionCommentLikedUsers, \
    LikeLikedByOtherUsersCommentInDisscussion, UnlikeLikedByOtherUsersCommentInDisscussion

from photo_page_elements import LikePhotoUnderPhoto, UnlikePhotoUnderPhoto, \
    PhotoLikedUsers, LikePhotoInTheRightPhotoCorner, UnlikePhotoInTheRightPhotoCorner, \
    LikeNotOpenedPhotoInAlbum, UnlikeNotOpenedPhotoInAlbum, PhotoLikedUsersInAlbum, \
    LikeButtonAvatarPhoto, UnlikeButtonAvatarPhoto, ListAvatarPhotoLikedUsers

from video_page_elements import LikeVideoButtonUnderPlayer, UnlikeVideoButtonUnderPlayer, \
    VideoLikedUsers, LikeVideoButtonInsidePlayer, UnlikeVideoButtonInsidePlayer, \
    ButtonInsidePlayerLikesController, CloseVideoButton


class Page(object):
    """Main `PageObject` class.

    """
    BASE_URL = 'https://ok.ru/'
    PATH = '/'

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class AuthPage(Page):
    """Page to auth in `ok.ru`.

    """
    PATH = '/'

    @property
    def auth_form(self):
        return AuthForm(self.driver)


class VideoPage(Page):

    PATH_VIDEOS = (
        '/video/192156796190',
        '/video/219099564753',
        '/video/193083279874',
        '/video/214043462216'
    )

    def open_video(self, index):
        self.PATH = self.PATH_VIDEOS[index]
        super(VideoPage, self).open()

    @property
    def like_button_under_player(self):
        return LikeVideoButtonUnderPlayer(self.driver)

    @property
    def unlike_button_under_player(self):
        return UnlikeVideoButtonUnderPlayer(self.driver)

    @property
    def like_button_inside_player(self):
        return LikeVideoButtonInsidePlayer(self.driver)

    @property
    def unlike_button_inside_player(self):
        return UnlikeVideoButtonInsidePlayer(self.driver)

    @property
    def list_of_liked_users(self):
        return VideoLikedUsers(self.driver)

    @property
    def button_inside_player_likes_controller(self):
        return ButtonInsidePlayerLikesController(self.driver)

    @property
    def close_video_button(self):
        return CloseVideoButton(self.driver)


class PhotoPage(Page):

    PATH_PHOTOS = (
        '/redbull/album/57789917888573/836118479933',
        '/redbull/album/57789917888573/836626874429'
    )
    PATH_ALBUM = '/redbull/album/57789917888573'

    def open_photo(self, index):
        self.PATH = self.PATH_PHOTOS[index]
        super(PhotoPage, self).open()

    def open_album(self):
        self.PATH = self.PATH_ALBUM
        super(PhotoPage, self).open()

    @property
    def like_button_under_photo(self):
        return LikePhotoUnderPhoto(self.driver)

    @property
    def unlike_button_under_photo(self):
        return UnlikePhotoUnderPhoto(self.driver)

    @property
    def like_button_right_photo_corner(self):
        return LikePhotoInTheRightPhotoCorner(self.driver)

    @property
    def unlike_button_right_photo_corner(self):
        return UnlikePhotoInTheRightPhotoCorner(self.driver)

    @property
    def like_button_in_album(self):
        return LikeNotOpenedPhotoInAlbum(self.driver)

    @property
    def unlike_button_in_album(self):
        return UnlikeNotOpenedPhotoInAlbum(self.driver)

    @property
    def list_liked_users(self):
        return PhotoLikedUsers(self.driver)

    @property
    def list_liked_users_in_album(self):
        return PhotoLikedUsersInAlbum(self.driver)

    @property
    def like_button_avatar_in_profile(self):
        return LikeButtonAvatarPhoto(self.driver)

    @property
    def unlike_button_avatar_in_profile(self):
        return UnlikeButtonAvatarPhoto(self.driver)

    @property
    def list_liked_avatar_liked_users(self):
        return ListAvatarPhotoLikedUsers(self.driver)


class DiscussionPage(Page):

    def open(self):
        super(DiscussionPage, self).open()
        self.links_to_discussion_chat.open()

    @property
    def links_to_discussion_chat(self):
        return OpenDiscussionLinksChain(self.driver)

    @property
    def like_button_under_comment(self):
        return LikeCommentInDisscussion(self.driver)

    @property
    def unlike_button_under_comment(self):
        return UnlikeCommentInDisscussion(self.driver)

    @property
    def like_button_under_comment_controller(self):
        return DiscussionCommentLikesController(self.driver)

    @property
    def list_liked_users(self):
        return DiscussionCommentLikedUsers(self.driver)

    @property
    def like_liked_by_other_users_button_under_comment(self):
        return LikeLikedByOtherUsersCommentInDisscussion(self.driver)

    @property
    def unlike_liked_by_other_users_button_under_comment(self):
        return UnlikeLikedByOtherUsersCommentInDisscussion(self.driver)


class UserProfilePage(Page):

    PATH = '/profile/575705241837'
