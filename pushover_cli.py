#!/usr/bin/env python

# Copyright (c) 2013 Nick Groenen <nick@groenen.me>

import argparse
import chump


def main():
    parser = argparse.ArgumentParser(description="Simple pushover client")
    parser.add_argument('--token', required=True, help="your application's API token")
    parser.add_argument('--user', required=True, help="the user/group key (not e-mail address) of your user (or you)")
    parser.add_argument('--message', required=True, help="your message")
    parser.add_argument('--title', default=None, help="your message's title, otherwise your app's name is used")
    parser.add_argument('--url', default=None, help="a supplementary URL to show with your message")
    parser.add_argument('--url-title', default=None, help="a title for your supplementary URL, otherwise just the URL is shown")
    parser.add_argument('--device', default=None, help="your user's device name to send the message directly to that device, rather than all of the user's devices")
    parser.add_argument('--priority', default=0, help="send as -1 to always send as a quiet notification, 1 to display as high-priority and bypass the user's quiet hours, or 2 to also require confirmation from the user")
    parser.add_argument('--callback', default=None, help="a publicly-accessible URL the Pushover servers will send a request to when the user has acknowledged your notification")
    parser.add_argument('--retry', default=30, help="how often (in seconds) to repeat the notification to the user in case of an emergency priority")
    parser.add_argument('--expire', default=86400, help="how many seconds your notification will continue to be retried for (every retry seconds) in case of an emergency priority")
    parser.add_argument('--sound', default=None, help="the name of one of the sounds supported by device clients to override the user's default sound choice")

    args = parser.parse_args()
    app = chump.Application(args.token)
    user = app.get_user(args.user)

    user.send_message(
        args.message,
        title=args.title,
        url=args.url,
        url_title=args.url_title,
        device=args.device,
        priority=args.priority,
        callback=args.callback,
        retry=args.retry,
        expire=args.expire,
        sound=args.sound,
    )


if __name__ == "__main__":
    main()
