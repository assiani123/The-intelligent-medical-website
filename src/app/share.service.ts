import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ShareService {
  x: any
  y: any
  constructor() {
    this.x = false
    this.y = false
  }
}
