package BusinessLayer;

import static java.lang.Math.abs;

public class IncomeStatement extends Report {

    public Tuple getProbability(double p_sub, double p_total) {
        //get a probability
        double x, p = 0; //double p = 0;
        Tuple tuple = new Tuple(p_sub / p_total, 1 - abs(p_sub / p_total));
        //  x = p_sub / p_total;
        //  p = 1 - abs(p_sub / p_total);

        //double p1 = (x,p) ;
        return tuple; //x, p;
    }

    public Tuple getPercentage(double p_sub, double p_total) {

        /**
         *         Assumes `p_sub` is a probability (of an event `sub` (for  )
         *
         * - Gets the percentage of sun (in relation to the sub (the expenses)
         *
         * - Assumes _sub is
         * gets the percentage of sun (in relation to the sub (the expenses) "
         */


        //   # totalPercent = 1#00
        Tuple tuple = new Tuple(p_sub * 100, p_total * 100);
        // x, p = getProbability(p_sub, p_total) ;

        // x = x * 100 ; //#p_sub / p_total ;  //# * 100

        // p = p * 100  ;//#1 - ( p_sub / p_total ) # * 100

        return tuple;
    }

    private static final class Tuple {
        double x = 0;
        double p = 0;

        public Tuple(double x, double p) {
            this.x = x;
            this.p = p;
        }

    }


}
