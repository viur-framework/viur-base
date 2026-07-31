import "@viur/webawesome/dist/styles/webawesome.css"
import '@viur/webawesome/dist/styles/themes/default.css';

import '@viur/webawesome/dist/components/button/button';
import '@viur/webawesome/dist/components/button-group/button-group';

import '@viur/webawesome/dist/components/icon/icon';
import '@viur/webawesome/dist/components/split-panel/split-panel';
import '@viur/webawesome/dist/components/input/input';
import '@viur/webawesome/dist/components/spinner/spinner';
import '@viur/webawesome/dist/components/callout/callout';
import '@viur/webawesome/dist/components/card/card';
import '@viur/webawesome/dist/components/tooltip/tooltip';
import '@viur/webawesome/dist/components/drawer/drawer';
import '@viur/webawesome/dist/components/slider/slider';
import '@viur/webawesome/dist/components/badge/badge';
import '@viur/webawesome/dist/components/switch/switch';
import '@viur/webawesome/dist/components/dialog/dialog';
import '@viur/webawesome/dist/components/select/select';
import '@viur/webawesome/dist/components/checkbox/checkbox';
import '@viur/webawesome/dist/components/avatar/avatar';
import '@viur/webawesome/dist/components/format-date/format-date';
import '@viur/webawesome/dist/components/tab-group/tab-group';
import '@viur/webawesome/dist/components/tab-panel/tab-panel';
import '@viur/webawesome/dist/components/tab/tab';
import '@viur/webawesome/dist/components/copy-button/copy-button';
import '@viur/webawesome/dist/components/details/details';
import '@viur/webawesome/dist/components/progress-bar/progress-bar';
import '@viur/webawesome/dist/components/tooltip/tooltip';



import  {setBasePath, registerIconLibrary} from '@viur/webawesome/dist/webawesome.js';
setBasePath("/app")

registerIconLibrary('icons', {
    resolver: name => `/app/icons/${name}.svg`,
    mutator: svg => svg.setAttribute('fill', 'currentColor'),
})

registerIconLibrary('logos', {
    resolver: name => `/app/logos/${name}.svg`,
})
