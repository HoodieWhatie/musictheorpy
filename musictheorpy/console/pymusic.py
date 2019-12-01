#!/usr/bin/env python3

import sys
import argparse

import musictheorpy.notes as notes
# from musictheorpy.console import parser

invalid_note_help = "You have entered an invalid note name. Valid notes are uppercase English letters A through G\n"\
                    "possibly followed by a qualifier. Valid qualifiers are #, ##, b, and bb. No qualifier represents\n"\
                    "a natural. For example, A#, C, D##, Bb, Cbb are all valid notes, while AB, H#, and F### are\n"\
                    "invalid. "

invalid_interval_help = "You have entered an invalid interval.\n" \
                        "Intervals are represented by a letter representing the quality, followed by the interval\n"\
                        "number. Qualifiers are m (minor), M (major), A (augmented), d (diminished), and P (perfect).\n"\
                        "Qualifiers are case sensitive and and follow the standard scheme from Western music theory\n"\
                        "that major, augmented, and perfect are capitalized, while diminished and minor are\n"\
                        "lowercase. Valid interval numbers are 0 through 15."


def main():
    parser = argparse.ArgumentParser()
    subs = parser.add_subparsers()

    intervals_parser = subs.add_parser('intervals')
    intervals_parser.set_defaults(func=intervals)
    scales_parser = subs.add_parser('scales')
    scales_parser.set_defaults(func=scales)

    intervals_parser.add_argument('starting_note')
    intervals_parser.add_argument('interval')
    intervals_parser.add_argument('-d', '--descend', action='store_true')

    scales_parser.add_argument('tonic')
    scales_parser.add_argument('-m', '--minor', choices=['harmonic', 'melodic', 'natural'])

    args = parser.parse_args()
    args.func(args)


def intervals(args):
    print(args.starting_note)
    print(args.interval)


def scales(args):
    print(args.tonic)
    if args.minor:
        print(args.minor)


# def oldintervals():
#     argparser = parser.PyMusicArgumentParser()
#     tmpnote, interval, descend = unpack_arguments(argparser)
#
#     note = validate_note(tmpnote)
#     if note is None:
#         print(invalid_note_help)
#         sys.exit()
#
#     if interval is None:
#         print(invalid_interval_help)
#         sys.exit()
#
#     article = "An" if interval.startswith('AUGMENTED') else "A"
#
#     if descend:
#         try:
#             bottom_note = note.descend_interval(interval)
#             print("%s %s descending from %s is %s.\n" % (article, interval.lower(), note, bottom_note))
#         except notes.InvalidIntervalError:
#             print("%s %s descending from %s results in an invalid note.\n" % (article, interval.lower(), note))
#         finally:
#             sys.exit()
#     else:
#         try:
#             top_note = note.ascend_interval(interval)
#             print("%s %s ascending from %s is %s.\n" % (article, interval.lower(), note, top_note))
#         except notes.InvalidIntervalError:
#             print("%s %s ascending from %s results in an invalid notes.\n" % (article, interval.lower(), note))
#         finally:
#             sys.exit()


def unpack_arguments(argparser):
    args = argparser.pack()
    note = args['starting_note']
    interval = args['interval']

    if args['descend']:
        descend = args['descend']
        return note, interval, descend

    return note, interval, False


def validate_note(notename):
    try:
        note = notes.Note(notename)
    except notes.NoteNameError:
        return None

    return note


if __name__ == '__main__':
    main()
