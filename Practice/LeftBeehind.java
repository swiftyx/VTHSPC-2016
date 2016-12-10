import java.util.Scanner;
public class LeftBeehind {
   public static void main(String[] args) {
      Scanner in = new Scanner(System.in);
      int i=0;
      String[] r = new String[15];
      while (true) {
         int n,m;
         if (in.hasNextInt()) {
            n=in.nextInt();
            m=in.nextInt();
         } else {
            break;
         }
         if (n==0&&m==0)
            break;
         if (m+n==13) {
            r[i] = "Never speak again.";
         } else if (n==m) {
            r[i] = "Undecided.";
         } else if (n>m) {
            r[i] = "To the convention.";
         } else if (n<m) {
            r[i] = "Left beehind.";
         }
         i++;
         if (i==15)
            break;

      }
      for (String s:r) {
         if (s==null) break;
         System.out.println(s);
      }
   }
}
