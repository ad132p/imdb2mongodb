#!/bin/python3
import sys
from pymongo import MongoClient

raw_dataset_dir = sys.argv[1]


def name_basics():

    mongo_client = MongoClient()
    db = mongo_client.IMDB
    name_basics_coll = db.nameBasics

    name_basics = open(''.join([raw_dataset_dir, "name.basics.tsv"]))
    header = name_basics.readline().replace("\n", "")
    list_header = header.split("\t")
    for x in name_basics.readlines():
        x = x.replace("\n", "")
        values = x.split("\t")
        values[4], values[5] = values[4].split(","), values[5].split(",")
        dict_document = dict(zip(list_header, values))
        name_basics_coll.insert_one(dict_document)


def title_akas():

    mongo_client = MongoClient()
    db = mongo_client.IMDB
    title_akas_coll = db.titleAkas

    title_akas = open(''.join([raw_dataset_dir, "title.akas.tsv"]))
    header = title_akas.readline().replace("\n", "")
    list_header = header.split("\t")
    for x in title_akas.readlines():
        x = x.replace("\n", "")
        values = x.split("\t")
        values[5], values[6] = values[5].split(","), values[6].split(",")
        dict_document = dict(zip(list_header, values))
        title_akas_coll.insert_one(dict_document)

def title_basics():

    mongo_client = MongoClient()
    db = mongo_client.IMDB
    title_basics_coll = db.titleBasics

    title_basics = open(''.join([raw_dataset_dir, "title.basics.tsv"]))
    header = title_basics.readline().replace("\n", "")
    list_header = header.split("\t")
    for x in title_basics.readlines():
        x = x.replace("\n", "")
        values = x.split("\t")
        values[8] = values[8].split(",")
        dict_document = dict(zip(list_header, values))
        title_basics_coll.insert_one(dict_document)

def title_crew():

    mongo_client = MongoClient()
    db = mongo_client.IMDB
    title_crew_coll = db.titleCrew

    title_crew = open(''.join([raw_dataset_dir, "title.crew.tsv"]))
    header = title_crew.readline().replace("\n", "")
    list_header = header.split("\t")
    for x in title_crew.readlines():
        x = x.replace("\n", "")
        values = x.split("\t")
        values[1], values[2] = values[1].split(","), values[2].split(",")
        dict_document = dict(zip(list_header, values))
        title_crew_coll.insert_one(dict_document)

def title_episode():

    mongo_client = MongoClient()
    db = mongo_client.IMDB
    title_episode_coll = db.titleEpisode

    title_episode = open(''.join([raw_dataset_dir, "title.episode.tsv"]))
    header = title_episode.readline().replace("\n", "")
    list_header = header.split("\t")
    for x in title_episode.readlines():
        x = x.replace("\n", "")
        values = x.split("\t")
        try:
            values[2] = int(values[2])
        except:
            values[2] = None
        try:
            values[3] = int(values[2])
        except:
            values[3] = None
        dict_document = dict(zip(list_header, values))
        title_episode_coll.insert_one(dict_document)

def title_principals():

    mongo_client = MongoClient()
    db = mongo_client.IMDB
    title_principals_coll = db.titlePrincipals

    title_principals = open(''.join([raw_dataset_dir, "title.principals.tsv"]))
    header = title_principals.readline().replace("\n", "")
    list_header = header.split("\t")
    for x in title_principals.readlines():
        x = x.replace("\n", "")
        values = x.split("\t")
        values[1] = int(values[1])
        try:
            values[1] = int(values[1])
        except:
            values[1] = None
        dict_document = dict(zip(list_header, values))
        title_principals_coll.insert_one(dict_document)

def title_ratings():

    mongo_client = MongoClient()
    db = mongo_client.IMDB
    title_ratings_coll = db.titleRatings

    title_ratings = open(''.join([raw_dataset_dir, "title.ratings.tsv"]))
    header = title_ratings.readline().replace("\n", "")
    list_header = header.split("\t")
    for x in title_ratings.readlines():
        x = x.replace("\n", "")
        values = x.split("\t")
        dict_document = dict(zip(list_header, values))
        title_ratings_coll.insert_one(dict_document)


name_basics()
title_akas()
title_basics()
title_crew()
title_episode()
title_principals()
title_ratings()


