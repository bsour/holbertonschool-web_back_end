import Building from "./5-building";

class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    if (typeof sqft === 'number' && typeof floors === 'number') {
      super(sqft);
      this._floors = floors;
    } else {
      throw Error('sqft and floors must be numbers');
    }
  }

  get floors() {
    return this._floors;
  }

  evacuationWarningMessage() {
    this._sqrt = this._sqft;
    throw new Error('Evacuate slowly the NUMBER_OF_FLOORS floors');
  }
}

export default SkyHighBuilding;
