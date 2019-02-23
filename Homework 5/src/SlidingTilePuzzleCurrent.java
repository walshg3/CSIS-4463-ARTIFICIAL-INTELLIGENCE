import csis4463.SlidingTilePuzzle;
import java.util.ArrayList;

public class SlidingTilePuzzleCurrent{
	private SlidingTilePuzzle stp;
	private ArrayList<SlidingTilePuzzle> path;

	public SlidingTilePuzzleCurrent(SlidingTilePuzzle stp){
		this.stp = stp;
		this.path = new ArrayList<SlidingTilePuzzle>();
		path.add(stp);
	}	

	private SlidingTilePuzzleCurrent(SlidingTilePuzzle stp, ArrayList<SlidingTilePuzzle> path){
		this.stp = stp;
		this.path = path;
		path.add(stp);

	}

	public ArrayList<SlidingTilePuzzle> getPath(){
		return path;
	}

	public int getPriority(){
		int manhattanDistance=0;

		for(int i=0;i<stp.numRows();i++){
			
			for(int j=0;j<stp.numColumns();j++){
				int tile = stp.getTile(i,j);
				int adjusted = tile==0 ? 8 : tile-1;
				int goalRow = adjusted/stp.numColumns();
				int goalColumn = adjusted%stp.numColumns();
				
				manhattanDistance += Math.abs(i-goalRow) + Math.abs(j-goalColumn);
				

			}

		}

		return manhattanDistance+path.size()-1;
		
	}
	
	/**
	 *  return unique string representation of board state the make a hashable value to use to look up board states
	 *  @return string representation of puzzle
	 */
	public String getHashValue(){

		StringBuilder sb = new StringBuilder();
		for(int i=0;i<stp.numRows();i++){
			
			for(int j=0;j<stp.numColumns();j++){
				
				sb.append(stp.getTile(i,j));

			}

		}

		return sb.toString();

	}

	public boolean isGoalState(){
		return stp.isGoalState();
	}

	public ArrayList<SlidingTilePuzzleCurrent> getSuccessors(){
		
		ArrayList<SlidingTilePuzzleCurrent> successors = new ArrayList<>(4);
		
		//box each successor into a wrapper 
		for(SlidingTilePuzzle puzzle : stp.getSuccessors()){
			successors.add(new SlidingTilePuzzleCurrent(puzzle,path));
		}

		return successors;
	}
}
