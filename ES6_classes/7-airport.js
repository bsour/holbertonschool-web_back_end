class Airport {
  constructor(name, code) {
    if (typeof name === 'string' && typeof code === 'string') {
      this._name = name;
      this._code = code;
    } else {
      throw Error('invalid input');
    }
  }

  toString() {
    return `Airport [${this._code}] { _name: ${this._name}, _code: '${this._code}' }`;
  }
}

export default Airport;
