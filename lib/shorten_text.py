import unicodedata


def shorten_text(base_text: str, n: int) -> str:
    """
    base_textを全角の指定文字数内に縮める
    :param base_text : 対象のテキスト
    :param n : 縮めたい全角文字数
    :return shortened : 全角n文字以内のテキスト
    """
    count = 0
    shortened = ""
    max_length = n * 2 - 1
    for c in base_text:
        # 半角max_length文字より大きくなったら抜ける
        if count > max_length:
            break
        if unicodedata.east_asian_width(c) in 'FWA':
            shortened = shortened + c
            count += 2
        else:
            shortened = shortened + c
            count += 1

    return shortened
