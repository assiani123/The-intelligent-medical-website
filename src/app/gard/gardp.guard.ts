import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, CanActivateChild, RouterStateSnapshot, UrlTree } from '@angular/router';

import { Observable } from 'rxjs';
import { ShareService } from '../share.service';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class GardpGuard implements CanActivate, CanActivateChild {
  constructor(private router: Router, private share: ShareService) {

  }


  canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {
    return new Promise((resolve, reject) => {
      if (this.share.y == true) {
        resolve(true);
      } else {
        this.router.navigate(['/']);
        resolve(false);
      }
    });
  }

  canActivateChild(
    childRoute: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {
    return new Promise((resolve, reject) => {
      if (this.share.y == true) {
        resolve(true);
      } else {
        this.router.navigate(['/']);
        resolve(false);
      }
    });
  }
}