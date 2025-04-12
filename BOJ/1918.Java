import java.util.*;

// 1918 후위 표기식

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        System.out.println(convert(input));
    }

    public static String convert(String exp) {
        String ret = "";
        Stack<Character> operator = new Stack(); //연산자

        for (int i=0; i<exp.length(); i++) {
            char c = exp.charAt(i);
            if (c == '(') {
                operator.push(c);
            } else if ( c == ')') {
                while ((!operator.isEmpty()) && operator.peek() != '(' ) {
                    ret += ""+operator.pop();
                }
                operator.pop(); // 여는 괄호
            } else if (c == '*' || c=='/') {
                if (!operator.isEmpty() && (operator.peek() == '*' || operator.peek() == '/')) {
                    ret += "" + operator.pop();
                }
                operator.push(c);
            } else if (c == '+' || c == '-') {
                if (!operator.isEmpty() && !(operator.peek() == '(')) {
                    while (!operator.isEmpty() && !(operator.peek() == '(')) {
                        ret += "" + operator.pop();
                    }
                }
                operator.push(c);
            } else { //피연산자들
                ret += ""+c;
            }
        }
        while ((!operator.isEmpty())) {
            char c = operator.pop();
            if (c == '(') {continue;}
            ret += ""+c;
        }
        return ret;
    }
}