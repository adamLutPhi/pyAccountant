package Interfaces;

public interface IAccountancy
/**
 * performs accounting equations  ( & anything about them)
 */
{
    /**
     * Finds the difference between the Left Hand Side `LHS` , & the Right Hand Side `RHS`
     * @param LHS
     * @param RHS
     * @return
     */
    // public JRule: No Redundancy
     double getDifference(double LHS, double RHS);

    /**
     *
     * @param totalAssets
     * @param totalLiabilities
     * @param totalEquities
     * @return
     */
     Boolean IsEqual(Double totalAssets, Double totalLiabilities, Double totalEquities);
     // totalAssets + totalLiabilities == totalEquities

    Boolean isBalanced(Double totalAssets, Double totalLiabilities, Double totalEquity );
}
