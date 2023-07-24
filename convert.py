import re
import pykakasi

def extract_japanese(source):
    # 行コメントとブロックコメントを除去
    no_comments = re.sub(r"(//.*|/\*[^*]*\*+(?:[^/*][^*]*\*+)*/)", "", source)

    # 日本語の単語を抽出（Unicodeの範囲を使用）
    japanese_words = re.findall(r"[\u2E80-\u2EFF\u3000-\u303F\u3040-\u309F\u30A0-\u30FF\u3200-\u32FF\u3300-\u33FF\u4E00-\u9FCC\uF900-\uFAD9\U00020000-\U0002FFFF]+", no_comments)

    # リストを返す
    return japanese_words

def word_to_romaji(japanese_words):
    kks = pykakasi.kakasi()
    romaji_list = []
    for word in japanese_words:
        result = kks.convert(word)
        romaji_list.append(''.join([item['hepburn'] for item in result]))
    return romaji_list


java_source = """
import java.util.ArrayList;
import java.util.List;

// 学生を管理するクラス
public class 学生管理 {
    private List<学生> 学生リスト;

    public 学生管理() {
        学生リスト = new ArrayList<>();
    }

    // ...
    // （省略）
    // ...

    public static void main(String[] args) {
        // 学生管理のインスタンスを生成
        学生管理 管理者 = new 学生管理();

        // 学生を追加
        管理者.学生追加(new 学生("田中", 20, "すうがく"));
        管理者.学生追加(new 学生("佐藤", 19, "エイゴ"));
        管理者.学生追加(new 学生("年金", 20, "市場１"));
        管理者.学生追加(new 学生("代行", 19, "キャッシュバランス再計算９９９９９"));

        // ...
        // （省略）
        // ...
    }
}
"""

# 日本語の単語の重複排除
unique_japanese_words = list(set(extract_japanese(java_source)))
print(unique_japanese_words)

# ローマ字に変換
print(word_to_romaji(unique_japanese_words))
