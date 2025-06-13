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
        'genre': '[B][COLOR purple]==filmes 2025==[/COLOR][/B]',
        'icon':
'https://i.postimg.cc/85Fd6zvY/unnamed.png',
        'fanart':
'https://i.postimg.cc/bN9FVXfC/Americanflix.jpg',
        'movies': [
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
       'plot': 'Em O Truque do Amor, dois irmãos, Vito (Antonio Folletto) e Antonello (Vincenzo Nemolato), enfrentam uma crise financeira que ameaça arrancar eles da linda e amada casa onde vivem em Nápoles. Desesperados, eles criam um plano audacioso: enganar Marina (Laura Adriani), uma rica herdeira solitária, fingindo ser fundadores de uma instituição de caridade. Vito, um pai solteiro que já superou muitos desafios, assume o papel principal na farsa. No entanto, à medida que ele se aproxima de Marina, descobre sua profunda infelicidade e solidão. O coração de Vito começa a vacilar, e o engano se transforma em uma autêntica história de amor. Enquanto Vito e Marina se aproximam, Antonello se torna cada vez mais ansioso para receber o dinheiro. A pressão aumenta, e Vito precisa escolher entre salvar sua família ou seguir seu coração.',               
    'movies': [
            {

 'title': '[B][COLOR gold]O Truque do Amor[/COLOR][/B]',
'fanart':
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfizEm2AYtODpwndpqiLsszdfmI4ifrqA7IQ&usqp=CAU',
                'url': 'https://drive.usercontent.google.com/download?id=1LhQyuT_jdsr0f7rAHRWVy1yUsS2R3Rj_&export=download',
                'poster': 'https://image.tmdb.org/t/p/w342/gi6xUdJgh2OyF4yM7YAGGwKgKYS.jpg',
                'plot': 'Em O Truque do Amor, dois irmãos, Vito (Antonio Folletto) e Antonello (Vincenzo Nemolato), enfrentam uma crise financeira que ameaça arrancar eles da linda e amada casa onde vivem em Nápoles. Desesperados, eles criam um plano audacioso: enganar Marina (Laura Adriani), uma rica herdeira solitária, fingindo ser fundadores de uma instituição de caridade. Vito, um pai solteiro que já superou muitos desafios, assume o papel principal na farsa. No entanto, à medida que ele se aproxima de Marina, descobre sua profunda infelicidade e solidão. O coração de Vito começa a vacilar, e o engano se transforma em uma autêntica história de amor. Enquanto Vito e Marina se aproximam, Antonello se torna cada vez mais ansioso para receber o dinheiro. A pressão aumenta, e Vito precisa escolher entre salvar sua família ou seguir seu coração.',
                'year': 2025,
            
            },
        ],
    },
#começo
{
        'genre': '[B][COLOR gold] Star Trek: Seção 31[/COLOR][/B]',
        'icon':
'https://image.tmdb.org/t/p/w342/4lwW5zp8o2WZqynQtRs7jXDpQh1.jpg',
        'fanart':
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQEJi_tnP8A4_PnQGLRz0fp6FVN2wgYM_RpLL9qOUpUqZK49cCtCeLqjPc&s=10',
        'movies': [
            {

 'title': '[B][COLOR gold] Star Trek: Seção 31[/COLOR][/B]',
'fanart':
'',
                'url': '#',
                'poster': 'https://image.tmdb.org/t/p/w342/4lwW5zp8o2WZqynQtRs7jXDpQh1.jpg',
                'plot': 'A Imperatriz Philippa Georgiou entra para uma divisão secreta da Frota Estelar. Com a missão de proteger a Federação dos Planetas Unidos, ela também deve enfrentar os erros de seu passado.',
                'year': 2025,
            
            },
        ],
    },
#fim
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
#começo
{
        'genre': '[B][COLOR gold] Farol da Ilusão[/COLOR][/B]',
        'icon':
'https://image.tmdb.org/t/p/w342/1FLLIBXhSrqtGlmgmKylBeEIOaJ.jpg',
        'fanart':
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNQR171QdgAMPfKxoljJxXdaR7rREQmCwDqwSTSmMVU42ivm5ktJr9WBHh&s=10',
        'movies': [
            {

 'title': '[B][COLOR gold] Farol da Ilusão[/COLOR][/B]',
'fanart':
'',
                'url': '#',
                'poster': 'https://image.tmdb.org/t/p/w342/1FLLIBXhSrqtGlmgmKylBeEIOaJ.jpg',
                'plot': 'Em Farol da Ilusão, uma família precisa lutar por sua sobrevivência enquanto está presa numa idílica ilha deserta. A pitoresca paisagem esconde um cotidiano extenuante e um realidade chocante. O passado retorna para assombrá-los e delata segredos obscuros que eles tentam esconder da filha mais nova Jana. Com a situação fora do controle e as condições da ilha se revelando debilitantes, o que eles entendem como ficção e realidade se perde, borrando a linha entre os dois campos. Os quatro precisam, então, lidar com as consequências das difíceis decisões e escolhas que enfrentam para continuar de pé. Um teste de esperança e resiliência coloca-os de frente para confissões complicadas.',
                'year': 2025,
            
            },
        ],
    },
#fim
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
        'genre': '[B][COLOR gold] Vítimas do Dia[/COLOR][/B]',
        'icon':
'https://image.tmdb.org/t/p/w342/qoohRRRIH67NN7vORNeVDARr2SK.jpg',
        'fanart':
'https://pbs.twimg.com/ext_tw_video_thumb/1878097499228893184/pu/img/VkQyHrCUAcT5ub5l.jpg:large',
        'movies': [
            {

 'title': '[B][COLOR gold] Vítimas do Dia[/COLOR][/B]',
'fanart':
'',
                'url': '#',
                'poster': 'https://image.tmdb.org/t/p/w342/qoohRRRIH67NN7vORNeVDARr2SK.jpg',
                'plot': 'Escrito por Dino Cantelli e com direção de Bruno Safadi, Vítimas do Dia acompanha um drama realista de uma noite decisiva na vida do casal Daiane (Jéssica Ellen) e Elder (Amaury Lorenzo), que esperam o primeiro filho, Davi. Próxima do fim de sua gestação, Daiane tem um desejo repentino e pede ao marido que compre uma fruta. Para atendê-la, Elder vai até o supermercado, onde fica preso após ser atingido por uma bala perdida, por conta de um intenso tiroteio nas proximidades. Ao tomar conhecimento do ocorrido, Daiane acaba entrando em trabalho de parto. Uma corrida contra o tempo tem início: de um lado, o pequeno Davi pede para nascer; do outro, Elder faz de tudo para sobreviver.',
                'year': 2025,
            
            },
        ],
    },
#fim

#começo
{
        'genre': '[B][COLOR gold]O Brutalista[/COLOR][/B]',
        'icon':
'https://image.tmdb.org/t/p/w342/vP7Yd6couiAaw9jgMd5cjMRj3hQ.jpg',
        'fanart':
'https://i.ytimg.com/vi/LK2gNeG8VIQ/maxresdefault.jpg',
        'movies': [
            {

 'title': '[B][COLOR gold]O Brutalista[/COLOR][/B]',
'fanart':
'',
                'url': '#',
                'poster': 'https://image.tmdb.org/t/p/w342/vP7Yd6couiAaw9jgMd5cjMRj3hQ.jpg',
                'plot': 'O Brutalista se passa em 1947, quando o arquiteto visionário húngaro László Toth (Adrien Brody) e sua esposa Erzsébet (Felicity Jones) fogem da Europa devastada pela guerra em busca de um novo começo na América. Em sua jornada para reconstruir seu legado e testemunhar o surgimento da América moderna, eles se deparam com uma oportunidade que pode mudar suas vidas para sempre. O industrial rico e carismático Harrison Van Buren (Guy Pearce) oferece a László um sonho americano em bandeja de prata: a chance de projetar um grandioso monumento modernista que moldará a paisagem do país que agora chamam de lar. Este projeto ambicioso representa o auge da carreira de László, prometendo levar ele e Erzsébet a novas alturas de sucesso e reconhecimento. No entanto, o caminho para a realização de seus sonhos é repleto de desafios e reveses inesperados, que os levarão a enfrentar tanto triunfos quanto tragédias ao longo de quase três décadas.',
                'year': 2025,
            
            },
        ],
    },
#fim

#começo
{
        'genre': '[B][COLOR gold]De Volta à Ação[/COLOR][/B]',
        'icon':
'https://image.tmdb.org/t/p/w342/m4gzzzeYRmrwasrBdJmjhBmjS3U.jpg',
        'fanart':
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQTMrmczABzJgmnatnEOr73P_i7Z7FqTWKMvA&usqp=CAU',
        'movies': [
            {

 'title': '[B][COLOR gold]De Volta à Ação[/COLOR][/B]',
'fanart':
'',
                'url': '#',
                'poster': 'https://image.tmdb.org/t/p/w342/m4gzzzeYRmrwasrBdJmjhBmjS3U.jpg',
                'plot': 'De Volta a Ação é um longa dirigido por Seth Gordon, roteirizado por Brendan O’Brien e estrelado por Cameron Diaz e Jamie Foxx. O filme vai retratar os ex-espiões da CIA, Emily (Cameron Diaz) e Matt (Jamie Foxx), que deixaram as suas carreiras para trás com a intenção de construírem uma família juntos, longe dos riscos que a espionagem podem apresentar. Entretanto, muitos anos depois de terem largado seus trabalhos, eles serão obrigados a voltar para o mundo da espionagem. Essa volta repentina deve-se ao fato das suas identidades secretas terem sido expostas. De Volta à Ação é uma celebração de amizade entre Cameron e Jamie, uma vez que eles já realizaram outros trabalhos juntos como Um Domingo Qualquer e Annie.',
                'year': 2025,
            
            },
        ],
    },
#fim

#começo
{
        'genre': '[B][COLOR gold]Paddington: Uma Aventura na Floresta[/COLOR][/B]',
        'icon':
'https://image.tmdb.org/t/p/w342/lmQnyeuRCDXf5MFNu3eyznO4FTn.jpg',
        'fanart':
'https://images.savoysystems.co.uk/KAK/685074.jpg',
        'movies': [
            {

 'title': '[B][COLOR gold]Paddington: Uma Aventura na Floresta[/COLOR][/B]',
'fanart':
'',
                'url': '#',
                'poster': 'https://image.tmdb.org/t/p/w342/lmQnyeuRCDXf5MFNu3eyznO4FTn.jpg',
                'plot': 'Em Paddington – Uma Aventura na Floresta, o adorável urso Paddington retorna ao Peru para visitar sua querida Tia Lucy, acompanhado pela família Brown. A viagem, que promete ser uma reunião afetuosa, logo se transforma em uma jornada cheia de surpresas e mistérios a serem resolvidos. Enquanto explora a floresta amazônica, Paddington e seus amigos encontram uma variedade de desafios inesperados e se deparam com a deslumbrante biodiversidade do local. Além de garantir muita diversão para o público, o filme aborda temas de amizade e coragem, proporcionando uma experiência emocionante para toda a família. Bruno Gagliasso, mais uma vez, empresta sua voz ao personagem na versão brasileira, adicionando um toque especial ao carismático urso. Com estreia marcada para 16 de janeiro, o longa promete encantar as crianças nas férias e já conquistou o público com um trailer inédito que antecipa as aventuras que aguardam Paddington e a família Brown no coração da Amazônia.',
                'year': 2025,
            
            },
        ],
    },
#fim
#começo
{
        'genre': '[B][COLOR gold] Imparável[/COLOR][/B]',
        'icon':
'https://image.tmdb.org/t/p/w342/dS7YrQ0nk5oYuYJDpEhYvBcdanl.jpg',
        'fanart':
'https://cdn.ome.lt/sqERhwiQIyktSsGza1FhU6_ixOY=/570x0/smart/uploads/conteudo/fotos/imparavel-critica-destaque.png',
        'movies': [
            {

 'title': '[B][COLOR gold] Imparável[/COLOR][/B]',
'fanart':
'',
                'url': '#',
                'poster': 'https://image.tmdb.org/t/p/w342/dS7YrQ0nk5oYuYJDpEhYvBcdanl.jpg',
                'plot': 'Anthony Robles, apesar de ter nascido sem a perna direita e ter crescido em um lar abusivo, se tornou um campeão de luta livre da NCAA Divisão 1, conquistando finalmente um campeonato nacional contra a escola que o rejeitou, a poderosa Universidade de Iowa. (Baseado no livro Unstoppable: From Underdog to Undefeated: How I Became a Champion, de Anthony Robles e Austin Murphy.)',
                'year': 2025,
            
            },
        ],
    },
#fim
#começo
{
        'genre': '[B][COLOR gold] Oficina do Diabo[/COLOR][/B]',
        'icon':
'https://image.tmdb.org/t/p/w342/1FLLIBXhSrqtGlmgmKylBeEIOaJ.jpg',
        'fanart':
'https://cdn.prod.website-files.com/60ff690cd7b0537edb99a29a/676ac5f86975233e174f9cd1_Filme%20Oficina%20do%20Diabo%20(2025).jpg',
        'movies': [
            {

 'title': '[B][COLOR gold] Oficina do Diabo[/COLOR][/B]',
'fanart':
'',
                'url': '#',
                'poster': 'https://image.tmdb.org/t/p/w342/1FLLIBXhSrqtGlmgmKylBeEIOaJ.jpg',
                'plot': 'Oficina do Diabo é um filme de drama que acompanha a empresa mais antiga do mundo: o inferno. O demônio Fausto, um dos principais colaboradores da empresa, subiu a Terra para ajudar Natan a devorar sua primeira alma, o protagonista Pedro. Após tentar a vida como músico na cidade grande, Pedro falhou devido à luxúria, desorganização e outros vícios que tomaram conta do seu coração. A volta a sua cidade no interior afetou seu ego, sua vida parece sem rumo. O demônio Natan regozijou-se com suas conquistas, mas suas tentações não estavam sendo suficientes para desvirtuá-lo completamente. Decididos a perder Pedro, o experiente demônio Fausto veio diretamente do inferno para guiar Natan em sua missão.',
                'year': 2025,
            
            },
        ],
    },
#fim
#começo
{
        'genre': '[B][COLOR gold] Covil de Ladrões 2[/COLOR][/B]',
        'icon':
'https://image.tmdb.org/t/p/w342/lwU8lY65QqcLOTVlZvL4Dse1h69.jpg',
        'fanart':
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSTsw0wPoB4R1l5jqpzZGlZs_Y68jTs4cZIsw&usqp=CAU',
        'movies': [
            {

 'title': '[B][COLOR gold] Covil de Ladrões 2[/COLOR][/B]',
'fanart':
'',
                'url': '#',
                'poster': 'https://image.tmdb.org/t/p/w342/lwU8lY65QqcLOTVlZvL4Dse1h69.jpg',
                'plot': 'Uma troca de lealdade coloca Big Nick (Gerard Butler) e Donnie (O’Shea Jackson Jr.) do mesmo lado numa operação perigosa. Em Covil de Ladrões 2, Big Nick está à procura de Donnie, que escapou da Europa e está planejando seu próximo plano: roubar uma carga de diamantes que equivale a mais de 800 milhões de euros do Centro de Diamantes, o prédio mais seguro da Europa Continental. Dessa vez, porém, Big Nick não está atrás de capturá-lo, mas sim está determinado a fazer parte do elaborado assalto organizado por Donnie e seu grupo, Os Panteras, deixando para trás seus dias de policial e xerife. O que ninguém imaginava era que, mergulhados no mundo complexo e imprevisível dos ladrões de pedras preciosas, o esquema deles envolveria os diamantes de outra máfia. Agora, é preciso escapar com vida de uma caçada letal com outros criminosos.',
                'year': 2025,
            
            },
        ],
    },
#fim
#começo
{
        'genre': '[B][COLOR gold] Peter Pan’s Neverland Nightmare[/COLOR][/B]',
        'icon':
'https://image.tmdb.org/t/p/w342/d68TPd4eeFeJ7J0lqShAggf41Ig.jpg',
        'fanart':
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhhmvyx8Ac45_vO5LDdkjhuQs0X2aw1wi1nw&usqp=CAU',
        'movies': [
            {

 'title': '[B][COLOR gold] Peter Pan’s Neverland Nightmare[/COLOR][/B]',
'fanart':
'',
                'url': '#',
                'poster': 'https://image.tmdb.org/t/p/w342/d68TPd4eeFeJ7J0lqShAggf41Ig.jpg',
                'plot': 'Wendy Darling sai em uma tentativa de resgatar seu irmão Michael das “garras do malvado Peter Pan”. Ao longo do caminho, ela conhece Tinkerbell, que será vista tomando heroína, acreditando ser pó de fada.',
                'year': 2025,
            
            },
        ],
    },
#fim
#começo
{
        'genre': '[B][COLOR gold] Lobisomem[/COLOR][/B]',
        'icon':
'https://image.tmdb.org/t/p/w342/nCZI9WCRaiWq6NcSulsgGsJPUDK.jpg',
        'fanart':
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-vJ54Bh14Atki8bAMt387dcVf5dc5LnxUZg&usqp=CAU',
        'movies': [
            {

 'title': '[B][COLOR gold] Lobisomem[/COLOR][/B]',
'fanart':
'',
                'url': '#',
                'poster': 'https://image.tmdb.org/t/p/w342/nCZI9WCRaiWq6NcSulsgGsJPUDK.jpg',
                'plot': 'A lua está cheia e o terror está à solta. Lobisomem, a mais recente criação da Blumhouse e do diretor e roteirista Leigh Whannell, conhecido por seu trabalho em O Homem Invisível, promete levar o público a um novo nível de pavor. Neste arrebatador conto de horror, um homem deve lutar para proteger a si mesmo e sua família quando eles se tornam alvos de um lobisomem mortal. À medida que a lua cheia ilumina a noite, o grupo é perseguido, aterrorizado e assombrado por uma criatura que personifica seus piores pesadelos. Com a tensão crescendo a cada momento e o perigo sempre à espreita, Lobisomem promete uma experiência cinematográfica intensa e inquietante, explorando o medo primal que surge quando o sobrenatural se torna uma ameaça real. Prepare-se para uma noite de terror que você nunca esquecerá.',
                'year': 2025,
            
            },
        ],
    },
#fim
#começo
{
        'genre': '[B][COLOR gold] Alarum[/COLOR][/B]',
        'icon':
'https://image.tmdb.org/t/p/w342/v313aUGmMNj6yNveaiQXysBmjVS.jpg',
        'fanart':
'https://images.justwatch.com/backdrop/323989009/s640/alarum',
        'movies': [
            {

 'title': '[B][COLOR gold] Alarum[/COLOR][/B]',
'fanart':
'',
                'url': '#',
                'poster': 'https://image.tmdb.org/t/p/w342/v313aUGmMNj6yNveaiQXysBmjVS.jpg',
                'plot': 'Em Alarum, um casal de espiões abandonam seus postos e fogem de sua agência para se casarem. Enquanto Joe (Scott Eastwood) e Laura (Willa Fitzgerald) vivem fora do radar e aproveitam sua lua de mel numa cabana de inverno remota dentro de um resort, seu esconderijo é descoberto e atacado por diferentes organizações de espiões. Todos suspeitam que Joe e Laura se juntaram a um grupo de elite formado por agentes desonestos e criminosos chamado Alarum e, com isso, roubaram um conjunto de informações poderosas. Os dois, então, são postos no meio de um fogo cruzado com uma rede internacional de inteligência que busca um disco rígido importante. Joe pede ajuda de Chester (Sylvester Stallone) para salvar Laura que está presa no resort sozinha tendo em lutar contra um grupo de homen armados atrás dela.',
                'year': 2025,
            
            },
        ],
    },
#fim

#começo
{
        'genre': '[B][COLOR gold] titulo do filme em amarelo[/COLOR][/B]',
        'icon':
'link-da-capa.jpg',
        'fanart':
'link-do-background.jpg',
        'movies': [
            {

 'title': '[B][COLOR gold] titulo do filme em amarelo[/COLOR][/B]',
'fanart':
'',
                'url': '#',
                'poster': 'link-da-capa.jpg',
                'plot': 'sinopse',
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

