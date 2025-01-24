# Copyright (C) 2025, Nirk.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
Example video plugin that is compatible with Kodi 20.x "Nexus" and above
"""
import os
import sys
from urllib.parse import urlencode, parse_qsl

import xbmcgui
import xbmcplugin
from xbmcaddon import Addon
from xbmcvfs import translatePath

# Get the plugin url in plugin:// notation.
URL = sys.argv[0]
# Get a plugin handle as an integer number.
HANDLE = int(sys.argv[1])
# Get addon base path
ADDON_PATH = translatePath(Addon().getAddonInfo('path'))
ICONS_DIR = os.path.join(ADDON_PATH, 'resources', 'images', 'icons')
FANART_DIR = os.path.join(ADDON_PATH, 'resources', 'images', 'fanart')

# instalador de pacotes do americanflix
# Here we use a hardcoded list of movies simply for demonstrating purposes
# In a "real life" plugin you will need to get info and links to video files/streams
# from some website or online service.
VIDEOS = [
    {
        'genre': '[B][COLOR blue]Filmes 2025[/COLOR][/B]',
        'icon':
'https://i.postimg.cc/85Fd6zvY/unnamed.png',
        'fanart':
'https://i.postimg.cc/bN9FVXfC/Americanflix.jpg',
        'info': [
            {
            },
        ],
    },
{
        'genre': '[B][COLOR gold]O Truque do Amor[/COLOR][/B]',
        'icon':
'https://image.tmdb.org/t/p/w342/gi6xUdJgh2OyF4yM7YAGGwKgKYS.jpg',
        'fanart':
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfizEm2AYtODpwndpqiLsszdfmI4ifrqA7IQ&usqp=CAU',
        'movies': [
            {

 'title': '[B][COLOR gold]O Truque do Amor[/COLOR][/B]',
'fanart':
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfizEm2AYtODpwndpqiLsszdfmI4ifrqA7IQ&usqp=CAU',
                'url': 'https://dhruvmirrorpremium1-5155281d9a96.herokuapp.com/152457/O+Truque+do+Amor+2025+%28DUBLADO%29.mp4?hash=AgADmQ',
                'poster': 'https://image.tmdb.org/t/p/w342/gi6xUdJgh2OyF4yM7YAGGwKgKYS.jpg',
                'plot': 'Em O Truque do Amor, dois irmãos, Vito (Antonio Folletto) e Antonello (Vincenzo Nemolato), enfrentam uma crise financeira que ameaça arrancar eles da linda e amada casa onde vivem em Nápoles. Desesperados, eles criam um plano audacioso: enganar Marina (Laura Adriani), uma rica herdeira solitária, fingindo ser fundadores de uma instituição de caridade. Vito, um pai solteiro que já superou muitos desafios, assume o papel principal na farsa. No entanto, à medida que ele se aproxima de Marina, descobre sua profunda infelicidade e solidão. O coração de Vito começa a vacilar, e o engano se transforma em uma autêntica história de amor. Enquanto Vito e Marina se aproximam, Antonello se torna cada vez mais ansioso para receber o dinheiro. A pressão aumenta, e Vito precisa escolher entre salvar sua família ou seguir seu coração.',
                'year': 2025,
            
            },
        ],
    },
{
        'genre': '[B][COLOR gold]O Homem que Quer Viver para Sempre[/COLOR][/B]',
        'icon':
'https://image.tmdb.org/t/p/w342/s6mdvaGWxdfLb23wWBO1gHdnMdG.jpg',
        'fanart':
'https://media-manager.noticiasaominuto.com/640/naom_677bb0e286564.webp?crop_params=eyJsYW5kc2NhcGUiOnsiY3JvcFdpZHRoIjoxMjU2LCJjcm9wSGVpZ2h0Ijo3MDcsImNyb3BYIjo0LCJjcm9wWSI6Nn0sInBvcnRyYWl0Ijp7ImNyb3BXaWR0aCI6Mzk5LCJjcm9wSGVpZ2h0Ijo3MDksImNyb3BYIjo0NDEsImNyb3BZIjo1fX0=',
        'movies': [
            {

 'title': '[B][COLOR gold]O Homem que Quer Viver para Sempre[/COLOR][/B]',
'fanart':
'https://media-manager.noticiasaominuto.com/640/naom_677bb0e286564.webp?crop_params=eyJsYW5kc2NhcGUiOnsiY3JvcFdpZHRoIjoxMjU2LCJjcm9wSGVpZ2h0Ijo3MDcsImNyb3BYIjo0LCJjcm9wWSI6Nn0sInBvcnRyYWl0Ijp7ImNyb3BXaWR0aCI6Mzk5LCJjcm9wSGVpZ2h0Ijo3MDksImNyb3BYIjo0NDEsImNyb3BZIjo1fX0=',
                'url': 'https://dhruvmirrorpremium1-5155281d9a96.herokuapp.com/152459/O+Homem+que+Quer+Viver+para+Sempre+2025+%28DUBLADO%29.mp4?hash=AgADmw',
                'poster': 'https://image.tmdb.org/t/p/w342/s6mdvaGWxdfLb23wWBO1gHdnMdG.jpg',
                'plot': 'Em O Homem Que Quer Viver Para Sempre, Bryan Johnson é um influenciador da longevidade que está disposto a investir sua fortuna em tecnologias para retardar seu envelhecimento. Neste tocante documentário, acompanhamos a história desse excêntrico milionário em sua obsessiva busca pela juventude eterna. Desafiando os limites da biologia, Bryan coloca seu corpo e seu dinheiro à mercê da tecnologia, explorando os caminhos extremos que ele percorre para tentar alcançar a imortalidade. O documentário revela até onde um homem está disposto a ir para desafiar o processo natural do envelhecimento e tentar conquistar o impossível.',
                'year': 2025,
            
            },
        ],
    },
{
        'genre': '[B][COLOR gold]Umjolo: Entre Dois Amores[/COLOR][/B]',
        'icon':
'https://image.tmdb.org/t/p/w342/m1aZxghCHlQK07xymiqs1C4YdqC.jpg',
        'fanart':
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMss4aAscdWs5frbC0i4ytYTVXBzac0rme36LINAWkWr5pOfacJ9Q6H3aN&s=10',
        'movies': [
            {

 'title': '[B][COLOR gold]Umjolo: Entre Dois Amores[/COLOR][/B]',
'fanart':
'',
                'url': 'https://dhruvmirrorpremium1-5155281d9a96.herokuapp.com/152465/Umjolo+Entre+Dois+Amores.mp4?hash=AgADlA',
                'poster': 'https://image.tmdb.org/t/p/w342/m1aZxghCHlQK07xymiqs1C4YdqC.jpg',
                'plot': 'Quem mais está escondendo segredos de Sizwe? Entre romances avassaladores e uma gravidez inesperada, a vida dele está cheia de reviravoltas.',
                'year': 2025,
            
            },
        ],
    },
#exemplo de codigo para não dar mais erros

{
        'genre': '[B][COLOR gold] Missão Porto Seguro[/COLOR][/B]',
        'icon':
'https://image.tmdb.org/t/p/w342/dcoc4C57lCpAzBr2qojFjRCKO9E.jpg',
        'fanart':
'https://m.media-amazon.com/images/S/pv-target-images/3a3a515e3c5db3e744cb4a5e9d9269dee100d1ef0be5ceebd1e6f99dc9ce6311._SX1080_FMjpg_.jpg',
        'movies': [
            {

 'title': '[B][COLOR gold] Missão Porto Seguro[/COLOR][/B]',
'fanart':
'',
                'url': 'https://dhruvmirrorpremium1-5155281d9a96.herokuapp.com/153218/Miss%C3%A3o+Porto+Seguro+2025+%28NACIONAL%29.mp4?hash=AgADww',
                'poster': 'https://image.tmdb.org/t/p/w342/dcoc4C57lCpAzBr2qojFjRCKO9E.jpg',
                'plot': 'Em Missão Porto Seguro, a policial Denise (Giovanna Lancellotti) precisa se enfiar no meio de uma viagem de formatura de alunos do terceiro ano do ensino médio para Porto Seguro, com a finalidade de obter informações que possam ajudá-la a desarmar e prender uma organização criminosa. Para concluir a sua missão dentro do prazo, a policial contará com ajuda da jovem Babi (Ademara) e de mais quatro adolescentes que estão ali na viagem em busca de curtição e aventura (Sophia Valverde, Igor Jansen, Letícia Pedro e Raphael Vicente). Essa equipe colocará a policial em situações cômicas e atrapalhas, como um concurso de dança com a Sheila Mello e a Sheila Carvalho. Além de concluir essa missão inteiramente perigosa e desafiadora, Denise terá que concluir uma outra tarefa ainda mais difícil de lidar, uma vez que envolve questões emocionais. Ela precisa da aprovação do seu delegado, que também é seu chefe e seu pai (Miguel Falabella).',
                'year': 2025,
            
            },
        ],
    },
#fim do exemplo
#inicio
{
        'genre': '[B][COLOR gold] Ad Vitam [/COLOR][/B]',
        'icon':
'https://image.tmdb.org/t/p/w342/dOpSxmD3FWfl6SK8SLXw9uwcO05.jpg',
        'fanart':
'https://64.media.tumblr.com/e747b8b201fc21bb15274397f8f42660/4f49947540f6477c-61/s1280x1920/753b0a41f64c10b08eb130c224b2c86610b86b57.jpg',
        'movies': [
            {

 'title': '[B][COLOR gold] Ad Vitam [/COLOR][/B]',
'fanart':
'',
                'url': 'https://dhruvmirrorpremium1-5155281d9a96.herokuapp.com/153220/Ad+Vitam+2025+%28DUBLADO%29.mp4?hash=AgADqg',
                'poster': 'https://image.tmdb.org/t/p/w342/dOpSxmD3FWfl6SK8SLXw9uwcO05.jpg',
                'plot': 'O passado volta para assombrar um homem nesse drama de ação. Ad Vitam acompanha Franck (Guillaume Canet) numa missão para salvar a vida de sua esposa grávida após a mulher ser sequestrada por um grupo criminoso misterioso. Encontrar Léo e entregar o que os bandidos querem fará Franck reviver seu tempo como integrante de um grupo de elite chamado GIGN. No meio de uma trama política complexa e correndo contra o tempo, Franck precisa reunir suas habilidades para desvendar um escândalo que se conecta ao seu turbulento passado; uma conspiração que pode estar fora do seu controle e o obriga a confrontar forças que achou ter deixado para trás. Ad Vitam é um suspense de ação repleto de caçadas perigosas e de tirar o fôlego.',
                'year': 2025,
            
            },
        ],
    },
#fim
#começo
{
        'genre': '[B][COLOR gold] September 5[/COLOR][/B]',
        'icon':
'https://image.tmdb.org/t/p/w342/3emldMXl1Q3p5yFUOZmBtuEn65C.jpg',
        'fanart':
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRp1iqgy1PNUUsp6E2lRRZt4XBCeJ1y2FXWMg&usqp=CAU',
        'movies': [
            {

 'title': '[B][COLOR gold] September 5[/COLOR][/B]',
'fanart':
'',
                'url': 'https://dhruvmirrorpremium1-5155281d9a96.herokuapp.com/153228/September.5.2024.720p.CAMRip.Dublado.mkv?hash=AgADXh',
                'poster': 'https://image.tmdb.org/t/p/w342/3emldMXl1Q3p5yFUOZmBtuEn65C.jpg',
                'plot': 'Em September 5, uma equipe de jornalistas esportivos precisa mudar sua cobertura radicalmente quando atletas são feitos de reféns dentro da Vila Olímpica. O drama histórico conta a história do Massacre de Munique, atentado que aconteceu nos Jogos Olímpicos de Verão de 1972 na Alemanha, a partir do ponto de vista da equipe de transmissão da ABC Sports. Na noite de 5 de setembro de 1972, um grupo terrorista chamado Setembro Negro invadiu a Vila Olímpica e fez 11 atletas da delegação israelense de reféns. Então, os jornalistas esportivos que estavam cobrindo o evento tiveram que mudar radicalmente a pauta para noticiar ao vivo o que estava acontecendo durante o sequestro que viria a se tornar o maior atentado terrorista a acontecer em um evento esportivo até hoje.',
                'year': 2025,
            
            },
        ],
    },
#fim


#começo
{
        'genre': '[B][COLOR red] O Assassino do Calendário [/COLOR][/B]',
        'icon':
'https://image.tmdb.org/t/p/w342/aUZutzzSNvE7IDchtBRlHPCLvjB.jpg',
         'fanart':
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_i6YdqJ-RzU1gv_RHLy64gbzjTbKypLbekw&usqp=CAU',
        'movies': [
            {

 'title': '[B][COLOR gold] O Assassino do Calendário[/COLOR][/B]',
'fanart':
'',
                'url': '#',
                'poster': 'https://image.tmdb.org/t/p/w342/aUZutzzSNvE7IDchtBRlHPCLvjB.jpg',
                'plot': 'Klara vai morrer hoje, a menos que mate o marido. O Assassino do Calendário deu a ela esse ultimato. Quando Jules começa seu turno da noite em uma linha direta para mulheres que estão indo sozinhas para casa, ele atende a ligação de Klara. Ele logo se torna sua última esperança de sobrevivência e corre contra o tempo para salvá-la. Baseado no thriller e best-seller alemão de Sebastian Fitzek.',
                'year': 2025,
            
            },
        ],
    },
#fim
]


def get_url(**kwargs):
    """
    Create a URL for calling the plugin recursively from the given set of keyword arguments.

    :param kwargs: "argument=value" pairs
    :return: plugin call URL
    :rtype: str
    """
    return '{}?{}'.format(URL, urlencode(kwargs))


def get_genres():
    """
    Get the list of video genres

    Here you can insert some code that retrieves
    the list of video sections (in this case movie genres) from some site or API.

    :return: The list of video genres
    :rtype: list
    """
    return VIDEOS


def get_videos(genre_index):
    """
    Get the list of videofiles/streams.

    Here you can insert some code that retrieves
    the list of video streams in the given section from some site or API.

    :param genre_index: genre index
    :type genre_index: int
    :return: the list of videos in the category
    :rtype: list
    """
    return VIDEOS[genre_index]


def list_genres():
    """
    Create the list of movie genres in the Kodi interface.
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(HANDLE, 'Public Domain Movies')
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(HANDLE, 'movies')
    # Get movie genres
    genres = get_genres()
    # Iterate through genres
    for index, genre_info in enumerate(genres):
        # Create a list item with a text label.
        list_item = xbmcgui.ListItem(label=genre_info['genre'])
        # Set images for the list item.
        list_item.setArt({'icon': genre_info['icon'], 'fanart': genre_info['fanart']})
        # Set additional info for the list item using its InfoTag.
        # InfoTag allows to set various information for an item.
        # For available properties and methods see the following link:
        # https://codedocs.xyz/xbmc/xbmc/classXBMCAddon_1_1xbmc_1_1InfoTagVideo.html
        # 'mediatype' is needed for a skin to display info for this ListItem correctly.
        info_tag = list_item.getVideoInfoTag()
        info_tag.setMediaType('video')
        info_tag.setTitle(genre_info['genre'])
        info_tag.setGenres([genre_info['genre']])
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=listing&genre_index=0
        url = get_url(action='listing', genre_index=index)
        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(HANDLE, url, list_item, is_folder)
    # Add sort methods for the virtual folder items
    xbmcplugin.addSortMethod(HANDLE, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(HANDLE)


def list_videos(genre_index):
    """
    Create the list of playable videos in the Kodi interface.

    :param genre_index: the index of genre in the list of movie genres
    :type genre_index: int
    """
    genre_info = get_videos(genre_index)
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(HANDLE, genre_info['genre'])
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(HANDLE, 'movies')
    # Get the list of videos in the category.
    videos = genre_info['movies']
    # Iterate through videos.
    for video in videos:
        # Create a list item with a text label
        list_item = xbmcgui.ListItem(label=video['title'])
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use only poster for simplicity's sake.
        # In a real-life plugin you may need to set multiple image types.
        list_item.setArt({'poster': video['poster']})
        # Set additional info for the list item via InfoTag.
        # 'mediatype' is needed for skin to display info for this ListItem correctly.
        info_tag = list_item.getVideoInfoTag()
        info_tag.setMediaType('movie')
        info_tag.setTitle(video['title'])
        info_tag.setGenres([genre_info['genre']])
        info_tag.setPlot(video['plot'])
        info_tag.setYear(video['year'])
        # Set 'IsPlayable' property to 'true'.
        # This is mandatory for playable items!
        list_item.setProperty('IsPlayable', 'true')
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=play&video=https%3A%2F%2Fia600702.us.archive.org%2F3%2Fitems%2Firon_mask%2Firon_mask_512kb.mp4
        url = get_url(action='play', video=video['url'])
        # Add the list item to a virtual Kodi folder.
        # is_folder = False means that this item won't open any sub-list.
        is_folder = False
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(HANDLE, url, list_item, is_folder)
    # Add sort methods for the virtual folder items
    xbmcplugin.addSortMethod(HANDLE, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    xbmcplugin.addSortMethod(HANDLE, xbmcplugin.SORT_METHOD_VIDEO_YEAR)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(HANDLE)


def play_video(path):
    """
    Play a video by the provided path.

    :param path: Fully-qualified video URL
    :type path: str
    """
    # Create a playable item with a path to play.
    # offscreen=True means that the list item is not meant for displaying,
    # only to pass info to the Kodi player
    play_item = xbmcgui.ListItem(offscreen=True)
    play_item.setPath(path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(HANDLE, True, listitem=play_item)


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring

    :param paramstring: URL encoded plugin paramstring
    :type paramstring: str
    """
    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring))
    # Check the parameters passed to the plugin
    if not params:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
        list_genres()
    elif params['action'] == 'listing':
        # Display the list of videos in a provided category.
        list_videos(int(params['genre_index']))
    elif params['action'] == 'play':
        # Play a video from a provided URL.
        play_video(params['video'])
    else:
        # If the provided paramstring does not contain a supported action
        # we raise an exception. This helps to catch coding errors,
        # e.g. typos in action names.
        raise ValueError(f'Invalid paramstring: {paramstring}!')


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
