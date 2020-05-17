#!/usr/bin/env python3
#!coding=utf-8
import newspaper
import argparse
from newspaper import Article
from pyfzf.pyfzf import FzfPrompt


fzf = FzfPrompt()


class News(object):
    def __init__(self):
        self.url = "https://www.bloomberg.co.jp/"
        self.arts = newspaper.build(self.url, memoize_articles=False)
        self.art_list = []

    def choice_article(self):
        for art in self.arts.articles:
            if(art.title == None or
               len(str(art.title).strip()) == 0):
                continue
            else:
                self.art_list.append(art.url+"\n" + str(art.title).strip())

        print(fzf.prompt(self.art_list))

    def show_article(self, url):
        article = Article(url)
        article.download()
        article.parse()
        print(article.text)


def parser():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-c', '--choice', action='store_true',
                        help='choice ariticle in Japan')
    parser.add_argument('-s', '--show',
                        help='show aritcle')
    args = parser.parse_args()
    return args


def main():
    opt = parser()
    news = News()
    news.choice_article() if opt.choice else None
    news.show_article(opt.show) if opt.show else None


main()
