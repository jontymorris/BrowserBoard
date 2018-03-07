from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context = {"updates": [
			{
				"id": "1",
				"url": "https://www.mangapanda.com/one-piece/896",
				"img": "https://s3.mangapanda.com/cover/one-piece/one-piece-l1.jpg"
			},
			{
				"id": "2",
				"url": "https://www.mangapanda.com/black-clover/147",
				"img": "https://s3.mangapanda.com/cover/black-clover/black-clover-l0.jpg"
			},
			{
				"id": "3",
				"url": "kissanime.ru/Anime/Dragon-Ball-Super/Episode-129?id=143543",
				"img": "https://myanimelist.cdn-dena.com/images/anime/7/74606.jpg"
			},
			{
				"id": "4",
				"url": "http://kissanime.ru/Anime/Overlord-II/Episode-009?id=143595&s=beta&pfail=1",
				"img": "http://kissanime.ru/Uploads/Etc/11-30-2017/19597854588022l.jpg"
			}
		]
	}

	return render(request, 'home/index.html', context)

def edit(request):
	context = {"updates": [
			{
				"id": "1",
				"url": "https://www.mangapanda.com/one-piece",
				"img": "https://s3.mangapanda.com/cover/one-piece/one-piece-l1.jpg",
			},
			{
				"id": "2",
				"url": "https://www.mangapanda.com/black-clover",
				"img": "https://s3.mangapanda.com/cover/black-clover/black-clover-l0.jpg"
			},
			{
				"id": "3",
				"url": "kissanime.ru/Anime/Dragon-Ball-Super",
				"img": "https://myanimelist.cdn-dena.com/images/anime/7/74606.jpg"
			},
			{
				"id": "4",
				"url": "http://kissanime.ru/Anime/Overlord-II",
				"img": "http://kissanime.ru/Uploads/Etc/11-30-2017/19597854588022l.jpg"
			}
		]
	}

	return render(request, 'home/edit.html', context)