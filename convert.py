import re

def extract_japanese(source):
    # 行コメントとブロックコメントを除去
    no_comments = re.sub(r"(//.*|/\*[^*]*\*+(?:[^/*][^*]*\*+)*/)", "", source)

    # 日本語を抽出（Unicodeの範囲を使用）
    japanese = re.findall(r"[\u2E80-\u2EFF\u3000-\u303F\u3040-\u309F\u30A0-\u30FF\u3200-\u32FF\u3300-\u33FF\u4E00-\u9FCC\uF900-\uFAD9\U00020000-\U0002FFFF]", no_comments)

    # リストを文字列に変換して返す
    return ''.join(japanese)

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
        管理者.学生追加(new 学生("田中", 20, "数学"));
        管理者.学生追加(new 学生("佐藤", 19, "英語"));

        // ...
        // （省略）
        // ...
    }
}
"""

print(extract_japanese(java_source))

