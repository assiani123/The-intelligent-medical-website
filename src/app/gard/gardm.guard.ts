import { Injectable } from '@angular/core';
import { CanActivate, CanActivateChild, Router, ActivatedRouteSnapshot, RouterStateSnapshot, UrlTree } from '@angular/router';
import { Observable } from 'rxjs';
import { ShareService } from '../share.service';

@Injectable({
  providedIn: 'root'
})
export class GardmGuard implements CanActivate, CanActivateChild {
  x: any;

  constructor(private router: Router, private share: ShareService) {

  }

  canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {
    return new Promise((resolve, reject) => {
      if (this.share.x == true) {
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
      if (this.share.x == true) {
        resolve(true);
      } else {
        this.router.navigate(['/']);
        resolve(false);
      }
    });
  }
}