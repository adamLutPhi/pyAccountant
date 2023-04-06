package BusinessLayer;

import Interfaces.IAccountancy;
import Interfaces.ICalculable;
import Interfaces.IJavaException;
import Interfaces.IRatio;
import org.jetbrains.annotations.NotNull;

import java.io.Serializable;
import java.util.AbstractMap;
import java.util.ArrayList;
import java.util.Map;
import java.util.Set;

import static java.lang.Math.abs;

public class Report implements IAccountancy, ICalculable, IJavaException, IRatio {

    public final static ArrayList<Double> subTotals = new ArrayList<Double>(); //0; //list
    /**
     * @param errorMsg : a message for the error occured
     */
    public static final String errorMsg = "ERROR: Unexpected Error is thrown, please recheck Input then retry";
    /**
     * @param exceptionMsg: a message about the exception occured
     */
    public static final String exceptionMsg = "ERROR: Unexpected Exception is thrown, please recheck Input then retry";

    /**
     * public void threadExample(MyInterface someMethod){ // implements a method of type `MyInterface`
     * <p>
     * new Thread(() ->
     * someMethod()).
     * start(); //this::someMethod) //error; thread container is not a functional interface
     * <p>
     * //.Thread(MyFunction)
     * //  start();
     * // void start() {
     * // }
     * }
     *
     * @Contract(pure = true)
     * private @Nullable Object someMethod() {
     * return null;
     * }
     */
    public static void printFunction() {
    }

    /**
     * @param LHS
     * @param RHS
     * @return
     */
    @Override
    public double getDifference(double LHS, double RHS) {
        /** /**
         * Finds the difference between the Left Hand Side `LHS` , & the Right Hand Side `RHS`
         * @param LHS: Left Hand Side
         * @param RHS: Right Hand Side
         * @return
         *
         * for NetWorth
        totalAssets + totalLiabilities == totalEquities **/
        return abs(LHS) - abs(RHS);
    }

    /**
     * @param totalAssets
     * @param totalLiabilities
     * @param totalEquities
     * @return
     */
    @Override
    public Boolean IsEqual(@NotNull Double totalAssets, Double totalLiabilities, Double totalEquities) {
        //double IsEqual(double totalAssets, double totalLiabilities, double totalEquities);
        // totalAssets + totalLiabilities == totalEquities

        if (totalAssets.equals(totalLiabilities + totalEquities)) {
            return true;
        } else if (!totalAssets.equals(totalLiabilities + totalEquities)) {
            return false;
        } else {
            throw new Error("something Unexpected occured, please try again later");
        }
    }

    // double IsEqual(double totalAssets, double totalLiabilities, double totalEquities){}

    // totalAssets + totalLiabilities == totalEquities
    // private Object MyFunction; //error this function is not applied /** Uncomment me to test **/

    /**
     * //1. theoretical part
     *
     * @FunctionalInterface public static interface MyFunction {
     * void apply();
     * }
     * <p>
     * MyFunction f = () -> System.out.println("Hello, World!");
     * <p>
     * // Applied part
     * public void execute(@org.jetbrains.annotations.NotNull MyFunction f) {
     * f.apply();
     * }
     * <p>
     * // SAM Type (model)
     * public interface MyInterface {
     * String doSomething(int param1, String param2);
     * }
     */
    // void execute(MyFunction f) {
    //     return;
    // }

    //SAM Type
    //if using java+8 lambda expressions

    //void execute
    //  new Thread(() -> System.out.println("Hello, World!"));

    //Rule: in java: each function is an object

    //2. function (processing) Part
    @Override
    public Boolean isBalanced(Double totalAssets, Double totalLiabilities, Double totalEquities) {
        /**
         *      Checks whether Accounts in the balanceSheet is balanced
         *      By checking whether totalAssets equals: `totalLiabilities` plut `totalEquities`
         *      Applies to the classical `Accounting Equation`
         *      As: Assets  = Liabilities + Equities
         *
         * */
        return totalAssets == totalLiabilities + totalEquities;
    }

    /**
     * @param subTotals
     * @return
     */
    @Override
    // @Contract(mutates = "this")
    public double iterateSubtotals(@NotNull ArrayList<Double> subTotals) {
        /**
         * sums up all items in the ArrayList `subTotals`
         */
        double _sum = 0;

        for (double item : subTotals) {

            _sum += item;
        }
        return _sum;

    }

    @Override
    public void throwError(String errorMsg) {

    }

    /**
     * @param exceptionMsg
     */
    @Override
    public void throwException(String exceptionMsg) {

    }

   // @Override
    public double cashRatio(double cash, double CurrentLiabilities) {
        /**
         * Cash Ratio = Cash / Current Liabilities.
         */
        return cash / CurrentLiabilities;
    }

    //    @Override
  //  public double currentRatio(double CurrentAssets, double CurrentLiabilities) {
   // }

    //@Override
   // public double quickRatio(double cashEquivalents, double aReceivable, double currentLiabilities) {
   // }

    @Override
    public Double cashRatio(Double cash, Double CurrentLiabilities) {
        /**
         * Cash Ratio = Cash / Current Liabilities.
         */
        return cash / CurrentLiabilities;
    }

    @Override
    public Double currentRatio(Double CurrentAssets, Double CurrentLiabilities) {
        /**
         *  CurrentRatio = CurrentAssets / CurrentLiabilities
         */
        return CurrentAssets / CurrentLiabilities;
    }

    @Override
    public Double quickRatio(Double cashEquivalents, Double aReceivable, Double currentLiabilities) {
        /**
         Quick Ratio = (Cash & Equivalents + Accounts Receivable (A/R) / CurrentLiabilities

         source: https://www.investopedia.com/terms/a/accountsreceivable.asp
         Key Takeaways:
         - Accounts receivable (AR) are an asset account on the balance sheet
         - that represents money due to a company in the short term.

         AR = Accounts receivable are created when a company lets a
         buyer purchase their goods or services on credit.


         */
        Double cashRecievable = cashEquivalents + aReceivable;
        Double quickRatio = cashRecievable / currentLiabilities ;
        return quickRatio ;
    }

    class namesPrices {
        private ArrayList<String> names = new ArrayList<>();
        private ArrayList<Double> prices = new ArrayList<>();

        public namesPrices() {
            ArrayList<String> names = new ArrayList();
            ArrayList<Double> prices = new ArrayList();

            HashMap<Integer, String> map = new HashMap<Integer, String>();//Creating HashMap
            map.put(1, "Mango");  //Put elements in Map
        }

        public namesPrices(ArrayList<String> names, ArrayList<Double> prices) {
            this.names = names;
            this.prices = prices;
        }

        //Add HashMap
        public class HashMap<String, Double> extends AbstractMap<String, Double> implements Map<String, Double>, Cloneable, Serializable {
            /**
             * @return
             */
            @NotNull
            @Override
            public Set<Entry<String, Double>> entrySet() {
                return null;
            }

            /**
             * If the specified key is not already associated with a value (or is mapped
             * to {@code null}) associates it with the given value and returns
             * {@code null}, else returns the current value.
             *
             * @param key   key with which the specified value is to be associated
             * @param value value to be associated with the specified key
             * @return the previous value associated with the specified key, or
             * {@code null} if there was no mapping for the key.
             * (A {@code null} return can also indicate that the map
             * previously associated {@code null} with the key,
             * if the implementation supports null values.)
             * @throws UnsupportedOperationException if the {@code put} operation
             *                                       is not supported by this map
             *                                       (<a href="{@docRoot}/java.base/java/util/Collection.html#optional-restrictions">optional</a>)
             * @throws ClassCastException            if the key or value is of an inappropriate
             *                                       type for this map
             *                                       (<a href="{@docRoot}/java.base/java/util/Collection.html#optional-restrictions">optional</a>)
             * @throws NullPointerException          if the specified key or value is null,
             *                                       and this map does not permit null keys or values
             *                                       (<a href="{@docRoot}/java.base/java/util/Collection.html#optional-restrictions">optional</a>)
             * @throws IllegalArgumentException      if some property of the specified key
             *                                       or value prevents it from being stored in this map
             *                                       (<a href="{@docRoot}/java.base/java/util/Collection.html#optional-restrictions">optional</a>)
             * @implSpec The default implementation is equivalent to, for this {@code map}:
             *
             * <pre> {@code
             * V v = map.get(key);
             * if (v == null)
             *     v = map.put(key, value);
             *
             * return v;
             * }</pre>
             *
             * <p>The default implementation makes no guarantees about synchronization
             * or atomicity properties of this method. Any implementation providing
             * atomicity guarantees must override this method and document its
             * concurrency properties.
             * @since 1.8
             */
            //      @Nullable
            //      @Override
            //      public Double putIfAbsent(String key, Double value) {
            //         return Map.super.putIfAbsent(key, value);
            //     }
        }
    }
    //{return;}

    //public <printFunction> double iterateSubtotals(subTotals, printFunction)

    //   public double iterateSubtotals(int subTotals, Object printFunction) { // object works
    //    return 0.0;
    // }

    /** double _sum = 0;*/
    //<DataType of array/List><Temp variable name>   : <Array/List to be iterated>
    // subTotals.size; Worst: make own length function

/**
 @Contract(mutates = "this")
 public static double iterateSubtotals(@NotNull ArrayList<Double> subTotals) {
 double _sum = 0;
 // for(int i = 0; i< subTotals.size; i++){
 for (double item : subTotals) {

 _sum += item;

 }
 return _sum;

 }
 **/
}
