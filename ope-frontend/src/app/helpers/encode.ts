export class EncodeHelper {
  static FromBase64(str: string): string
  {
      const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';
      let output = '';

      str = String(str).replace(/=+$/, '');

      if ( str.length % 4 === 1 )
      {
          throw new Error(
              '\'atob\' failed: The string to be decoded is not correctly encoded.'
          );
      }

      /* tslint:disable */
      for (
          // initialize result and counters
          let bc = 0, bs: any, buffer: any, idx = 0;
          // get next character
          (buffer = str.charAt(idx++));
          // character found in table? initialize bit storage and add its ascii value;
          ~buffer &&
          (
              (bs = bc % 4 ? bs * 64 + buffer : buffer),
                  // and if not first of each 4 characters,
                  // convert the first 8 bits to one ascii character
              bc++ % 4
          )
              ? (output += String.fromCharCode(255 & (bs >> ((-2 * bc) & 6))))
              : 0
      )
      {
          // try to find character in table (0-63, not found => -1)
          buffer = chars.indexOf(buffer);
      }
      /* tslint:enable */

      return output;
  }
}
