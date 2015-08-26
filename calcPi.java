import java.util.Scanner;
import java.lang.Math;
import java.util.Random;

public class calcPi {

    public static void main (String[] args) {

        int n, hits, i;
        double theta, d, pi;
        Random r;

        Scanner console = new Scanner(System.in);
        System.out.print("Input the number  of pins to drop: ");
        n = console.nextInt();

        r = new Random();
        hits = 0;

        for (i = 0; i < n; i++){
            theta = r.nextDouble()*Math.PI;
            d = r.nextDouble()*0.5;
            if (d <= 0.5*Math.sin(theta)) hits++;
        }
        pi = 2.*(double)n/(double)hits;
        System.out.println("Pi ~= "+pi);
        System.out.println("calculated pi to "+(Math.abs((pi-Math.PI)/Math.PI)*100)+"%");

    }

}
