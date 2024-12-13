from gooey import Gooey, GooeyParser


@Gooey()
def main1():
    parser = GooeyParser()
    sp = parser.add_subparsers(dest="multitab")
    ad_ag1 = sp.add_parser("tab1")
    ad_ag1.add_argument("var1")

    ad_ag2 = sp.add_parser("tab2")
    ad_ag2.add_argument("var2")
    args = parser.parse_args()
    return args





